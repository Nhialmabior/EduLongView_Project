from typing import TypedDict, Any
class AgentState(TypedDict, total=False):
    run_id:str
    learner_id:str
    teacher_request:str
    history:dict
    evidence:list
    patterns:list
    gaps:list
    summary:str
    error:str
