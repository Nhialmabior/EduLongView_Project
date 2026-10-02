from fastapi import APIRouter
from database.database import get_connection
router=APIRouter(prefix="/api/audit",tags=["audit"])
@router.get("")
def logs():
    with get_connection() as c: return [dict(x) for x in c.execute("SELECT * FROM audit_log ORDER BY id DESC LIMIT 100").fetchall()]
