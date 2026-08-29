from fastapi import FastAPI
from .config import APP_ENV, SUPABASE_URL

app = FastAPI(title="MANORAKSHA API", version="0.1.0")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "manoraksha-api",
        "environment": APP_ENV,
        "supabase_configured": bool(SUPABASE_URL),
    }
