from fastapi import FastAPI
from .config import APP_ENV, SUPABASE_URL
from .chat import router as chat_router

app = FastAPI(title="MANORAKSHA API", version="0.1.0")

app.include_router(chat_router, prefix="/api")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "manoraksha-api",
        "environment": APP_ENV,
        "supabase_configured": bool(SUPABASE_URL),
    }
