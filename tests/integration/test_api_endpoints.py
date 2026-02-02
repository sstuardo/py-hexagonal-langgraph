"""Tests de los endpoints de la API con TestClient."""

from fastapi.testclient import TestClient
from langgraph.checkpoint.memory import MemorySaver

from py_hexagonal_langgraph.infrastructure.adapters.mock_llm_adapter import (
    MockLLMAdapter,
)
from py_hexagonal_langgraph.infrastructure.api.app import create_app
from py_hexagonal_langgraph.infrastructure.graph import build_graph


def test_chat_endpoint_returns_response() -> None:
    """El endpoint /chat devuelve la respuesta del asistente."""
    mock_llm = MockLLMAdapter(responses=["Respuesta de test desde API"])
    graph = build_graph(llm_adapter=mock_llm, checkpointer=MemorySaver())
    app = create_app(graph=graph)

    client = TestClient(app)
    response = client.post(
        "/chat",
        json={"message": "Hola", "thread_id": "api-test"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["response"] == "Respuesta de test desde API"
    assert data["thread_id"] == "api-test"


def test_health_endpoint() -> None:
    """El endpoint /health devuelve status ok."""
    app = create_app()
    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
