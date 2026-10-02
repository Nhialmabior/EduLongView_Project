from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agent.graph import analyze
from services.audit_service import new_run_id,audit
router=APIRouter(prefix="/api/agent",tags=["agent"])
class AnalyzeRequest(BaseModel):
    learner_id:str
    teacher_request:str="Analyze the learner's longitudinal development."

@router.post("/analyze")
def run(req:AnalyzeRequest):
    run_id=new_run_id()
    try: return analyze(req.learner_id,req.teacher_request,run_id,audit)
    except ValueError as e: raise HTTPException(404,str(e))
    except Exception as e: raise HTTPException(500,str(e))
