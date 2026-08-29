from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI

from .config import OPENAI_API_KEY, AI_PROVIDER


router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    if not OPENAI_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY is not configured"
        )

    if AI_PROVIDER.lower() != "openai":
        raise HTTPException(
            status_code=500,
            detail="AI_PROVIDER must be set to openai"
        )

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

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

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="AI request failed"
        )
