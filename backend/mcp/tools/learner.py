from services.learner_service import history, get_learner
def get_learner_history(learner_id: str):
    data=history(learner_id)
    if not data["learner"]: raise ValueError("Learner not found")
    return data
