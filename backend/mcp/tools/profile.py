import json
from datetime import datetime, timezone
from database.database import get_connection
def update_learner_profile(learner_id, pattern, category, confidence, evidence_ids, teacher_id, approval_id):
    with get_connection() as c:
        review=c.execute("SELECT decision FROM reviews WHERE run_id=? AND decision='approved' AND teacher_id=? ORDER BY id DESC LIMIT 1",(approval_id,teacher_id)).fetchone()
        if not review:
            raise PermissionError("Human approval required before profile update")
        c.execute("INSERT INTO profiles(learner_id,pattern,category,confidence,evidence_ids,teacher_id,approval_id,created_at) VALUES(?,?,?,?,?,?,?,?)",
            (learner_id,pattern,category,confidence,json.dumps(evidence_ids),teacher_id,approval_id,datetime.now(timezone.utc).isoformat()))
    return {"status":"updated","learner_id":learner_id,"approval_id":approval_id}
