import json
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database.database import get_connection
from mcp.tools.profile import update_learner_profile
from services.audit_service import audit
router=APIRouter(prefix="/api/reviews",tags=["reviews"])
class Review(BaseModel):
    run_id:str; learner_id:str; teacher_id:str="demo-teacher"; decision:str; patterns:list=[]; edited_summary:str|None=None

@router.post("")
def review(r:Review):
    if r.decision not in ("approved","rejected","edited"): raise HTTPException(400,"Invalid decision")
    now=datetime.now(timezone.utc).isoformat()
    with get_connection() as c:
        c.execute("INSERT INTO reviews(run_id,learner_id,teacher_id,decision,original_json,edited_json,created_at) VALUES(?,?,?,?,?,?,?)",
                  (r.run_id,r.learner_id,r.teacher_id,r.decision,json.dumps(r.patterns),json.dumps({"summary":r.edited_summary}) if r.edited_summary else None,now))
    audit(r.run_id,r.learner_id,r.teacher_id,"human_review",output_data={"decision":r.decision})
    if r.decision in ("approved","edited") and r.patterns:
        for p in r.patterns:
            update_learner_profile(r.learner_id,p["pattern"],p["category"],p["confidence"],p["evidence_ids"],r.teacher_id,r.run_id)
        audit(r.run_id,r.learner_id,r.teacher_id,"profile_updated","update_learner_profile",status="success")
    return {"status":"recorded","decision":r.decision}
