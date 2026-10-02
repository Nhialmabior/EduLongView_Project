from agent.state import AgentState
from mcp.tools.learner import get_learner_history
from mcp.tools.evidence import get_evidence
from mcp.tools.summary import draft_teacher_summary

def analyze(learner_id:str, teacher_request:str, run_id:str, audit_fn):
    audit_fn(run_id,learner_id,"agent","start",output_data={"request":teacher_request})
    try:
        h=get_learner_history(learner_id)
        audit_fn(run_id,learner_id,"agent","retrieve_history","get_learner_history",{"learner_id":learner_id},h)
        ev=get_evidence(learner_id)
        audit_fn(run_id,learner_id,"agent","retrieve_evidence","get_evidence",{"learner_id":learner_id},{"count":len(ev)})
        scores={}
        for x in h["assessments"]:
            scores.setdefault(x["subject"],[]).append(x["score"])
        patterns=[]
        for subject,vals in scores.items():
            if len(vals)>=2 and vals[-1]-vals[0]>=8:
                ids=[x["evidence_id"] for x in h["assessments"] if x["subject"]==subject]
                patterns.append({"category":"emerging strength","pattern":f"{subject} shows improvement across available assessments","confidence":"High" if len(vals)>=3 else "Moderate","evidence_ids":ids})
        if any(x["subject"]=="Pretechnical" and x["score"]>=85 for x in h["assessments"]):
            ids=[x["evidence_id"] for x in h["assessments"] if x["subject"]=="Pretechnical"]
            patterns.append({"category":"practical learning","pattern":"Strong performance in practical/pretechnical work","confidence":"Moderate","evidence_ids":ids})
        gaps=[]
        terms={x["term"] for x in h["assessments"]}
        for term in ["2025-T1","2025-T2","2026-T1"]:
            if term not in terms: gaps.append(f"No assessment records found for {term}.")
        summary=draft_teacher_summary(patterns,gaps)
        audit_fn(run_id,learner_id,"agent","analysis_complete",output_data={"patterns":patterns,"gaps":gaps})
        return {"run_id":run_id,"learner":h["learner"],"patterns":patterns,"gaps":gaps,"summary":summary,"status":"awaiting_review"}
    except Exception as e:
        audit_fn(run_id,learner_id,"agent","error",status="failed",output_data={"error":str(e)})
        raise
