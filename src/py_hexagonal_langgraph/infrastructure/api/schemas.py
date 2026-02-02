"""Schemas Pydantic para request/response."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request para el endpoint de chat."""

    message: str = Field(..., min_length=1, description="Mensaje del usuario")
    thread_id: str = Field(default="default", description="ID del hilo de conversación")


class ChatResponse(BaseModel):
    """Response del endpoint de chat."""

    response: str = Field(..., description="Respuesta del asistente")
    thread_id: str = Field(..., description="ID del hilo")
