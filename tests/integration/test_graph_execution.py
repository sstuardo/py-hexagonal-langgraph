"""Tests del grafo con MockLLMAdapter. Sin llamadas a API."""

from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver

from py_hexagonal_langgraph.infrastructure.adapters.mock_llm_adapter import (
    MockLLMAdapter,
)
from py_hexagonal_langgraph.infrastructure.graph import build_graph


def test_graph_invocation_returns_expected_state() -> None:
    """El grafo invocado con mock devuelve el estado esperado."""
    mock_llm = MockLLMAdapter(responses=["Hola, soy el asistente"])
    graph = build_graph(llm_adapter=mock_llm, checkpointer=MemorySaver())

    result = graph.invoke(
        {"messages": [HumanMessage(content="Hola")]},
        config={"configurable": {"thread_id": "test-1"}},
    )

    assert len(result["messages"]) == 2
    assert result["messages"][0].content == "Hola"
    assert result["messages"][-1].content == "Hola, soy el asistente"


def test_individual_node_execution() -> None:
    """Se puede invocar un nodo individual para tests aislados."""
    mock_llm = MockLLMAdapter(responses=["Respuesta del nodo"])
    graph = build_graph(llm_adapter=mock_llm, checkpointer=MemorySaver())

    agent_node = graph.nodes["agent"]
    result = agent_node.invoke(
        {"messages": [HumanMessage(content="Test")]},
    )

    assert "messages" in result
    assert len(result["messages"]) == 1
    assert result["messages"][0].content == "Respuesta del nodo"
