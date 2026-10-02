from services.learner_service import history
def get_evidence(learner_id: str, subject: str|None=None, term: str|None=None):
    h=history(learner_id)
    evidence=h["assessments"]+[
        {**x,"subject":"Observation","type":"observation","score":None} for x in h["observations"]
    ]
    if subject: evidence=[x for x in evidence if x.get("subject")==subject]
    if term: evidence=[x for x in evidence if x.get("term")==term]
    return evidence
