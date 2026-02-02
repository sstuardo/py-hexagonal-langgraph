"""Aplicación FastAPI y router."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver

from py_hexagonal_langgraph.infrastructure.adapters.openai_adapter import (
    OpenAIAdapter,
)
from py_hexagonal_langgraph.infrastructure.api.schemas import (
    ChatRequest,
    ChatResponse,
)
from py_hexagonal_langgraph.infrastructure.config import Settings
from py_hexagonal_langgraph.infrastructure.graph import build_graph

_settings = Settings()
_llm_adapter = OpenAIAdapter(api_key=_settings.openai_api_key)
_checkpointer = MemorySaver()
_compiled_graph = build_graph(
    llm_adapter=_llm_adapter,
    checkpointer=_checkpointer,
)


def create_app(
    graph: Any | None = None,
) -> FastAPI:
    """Factory para crear la app. Permite inyectar el grafo en tests."""
    app = FastAPI(title="py-hexagonal-langgraph", version="0.1.0")
    compiled = graph if graph is not None else _compiled_graph

    @app.post("/chat", response_model=ChatResponse)
    def chat(request: ChatRequest) -> ChatResponse:
        config: dict[str, Any] = {
            "configurable": {"thread_id": request.thread_id},
        }
        result = compiled.invoke(
            {"messages": [HumanMessage(content=request.message)]},
            config=config,
        )
        messages = result.get("messages", [])
        last_content = messages[-1].content if messages else "No se recibió respuesta"
        return ChatResponse(response=last_content, thread_id=request.thread_id)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
