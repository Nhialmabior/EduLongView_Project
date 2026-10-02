import json, uuid
from datetime import datetime, timezone
from database.database import get_connection

def audit(run_id, learner_id, actor, step, tool_name=None, input_data=None, output_data=None, status="success"):
    with get_connection() as c:
        c.execute(
            "INSERT INTO audit_log(run_id,learner_id,actor,step,tool_name,input_json,output_json,status,created_at) VALUES(?,?,?,?,?,?,?,?,?)",
            (run_id, learner_id, actor, step, tool_name, json.dumps(input_data or {}), json.dumps(output_data or {}), status, datetime.now(timezone.utc).isoformat())
        )

def new_run_id(): return "RUN-" + uuid.uuid4().hex[:10].upper()
