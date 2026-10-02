# Architecture

Teacher UI → FastAPI → LangGraph-compatible analysis workflow → MCP tools → SQLite/synthetic evidence → human review → audit log.

The main workflow deliberately pauses before profile writes. The frontend is presentation; the backend enforces approval.
