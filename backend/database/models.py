from .database import get_connection

def init_db():
    with get_connection() as c:
        c.executescript('''
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            learner_id TEXT NOT NULL,
            pattern TEXT NOT NULL,
            category TEXT NOT NULL,
            confidence TEXT NOT NULL,
            evidence_ids TEXT NOT NULL,
            teacher_id TEXT NOT NULL,
            approval_id TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id TEXT NOT NULL,
            learner_id TEXT,
            actor TEXT NOT NULL,
            step TEXT NOT NULL,
            tool_name TEXT,
            input_json TEXT,
            output_json TEXT,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id TEXT NOT NULL,
            learner_id TEXT NOT NULL,
            teacher_id TEXT NOT NULL,
            decision TEXT NOT NULL,
            original_json TEXT NOT NULL,
            edited_json TEXT,
            created_at TEXT NOT NULL
        );
        ''')
