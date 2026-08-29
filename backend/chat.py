from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY is not configured"
        )

    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions=(
                "You are MANORAKSHA, a supportive mental-health "
                "conversation assistant. Be empathetic, calm and "
                "safety-focused. You are not a replacement for "
                "professional or emergency care."
            ),
            input=request.message,
        )

        return {
            "reply": response.output_text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="AI request failed"
        )
