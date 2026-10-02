from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.models import init_db
from api.routes.learners import router as learners_router
from api.routes.agent import router as agent_router
from api.routes.reviews import router as reviews_router
from api.routes.audit import router as audit_router
init_db()
app=FastAPI(title="EduLongView API",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
app.include_router(learners_router); app.include_router(agent_router); app.include_router(reviews_router); app.include_router(audit_router)
@app.get("/api/health")
def health(): return {"status":"ok","service":"EduLongView"}
