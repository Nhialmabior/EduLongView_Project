from fastapi import APIRouter, HTTPException
from services.learner_service import learners, history, get_learner
router=APIRouter(prefix="/api/learners",tags=["learners"])
@router.get("")
def list_learners(): return learners()
@router.get("/{learner_id}")
def learner(learner_id:str):
    x=history(learner_id)
    if not x["learner"]: raise HTTPException(404,"Learner not found")
    return x
