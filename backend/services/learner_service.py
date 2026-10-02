import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def load(name):
    return json.loads((ROOT/"data"/name).read_text(encoding="utf-8"))
def learners(): return load("learners.json")
def assessments(): return load("assessments.json")
def attendance(): return load("attendance.json")
def observations(): return load("observations.json")
def activities(): return load("activities.json")
def get_learner(learner_id):
    return next((x for x in learners() if x["learner_id"]==learner_id), None)
def history(learner_id):
    return {
        "learner": get_learner(learner_id),
        "assessments":[x for x in assessments() if x["learner_id"]==learner_id],
        "attendance":[x for x in attendance() if x["learner_id"]==learner_id],
        "observations":[x for x in observations() if x["learner_id"]==learner_id],
        "activities":[x for x in activities() if x["learner_id"]==learner_id]
    }
