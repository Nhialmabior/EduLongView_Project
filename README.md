# EduLongView

EduLongView is a human-centred, evidence-grounded agentic AI prototype for teachers. It analyzes synthetic learner records across terms, retrieves supporting evidence through MCP tools, generates a draft learner profile, and requires teacher approval before consequential profile updates.

## Stack
- React + Vite
- FastAPI
- LangGraph-compatible agent workflow
- MCP-style Python server
- SQLite
- Ollama-compatible open-weight model configuration

## Quick start

### Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m database.seed
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

The frontend defaults to `http://localhost:5173` and the API to `http://localhost:8000`.

This prototype uses synthetic learner data only. The model integration is configurable; the demo includes a deterministic evidence-grounded analysis fallback so the core workflow can run without a model service.

See `docs/ARCHITECTURE.md`, `docs/MCP.md`, `docs/EVALS.md`, and `docs/DEMO_SCRIPT.md`.
