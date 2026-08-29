import os

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI

from .config import AI_API_KEY, AI_PROVIDER


router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    if not AI_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="AI_API_KEY is not configured"
        )

    if AI_PROVIDER.lower() != "openai":
        raise HTTPException(
            status_code=500,
            detail="AI_PROVIDER must be set to openai"
        )

    client = OpenAI(api_key=AI_API_KEY)

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions=(
                "You are MANORAKSHA, a supportive mental-health "
                "conversation assistant. Be empathetic, calm, respectful "
                "and safety-focused. Do not claim to be a doctor or "
                "mental-health professional. Encourage professional or "
                "emergency help when appropriate."
            ),
            input=request.message,
        )

        return {
            "reply": response.output_text
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="AI request failed"
        )
