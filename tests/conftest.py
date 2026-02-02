"""Fixtures compartidas: mock adapters, graph compilado."""

import pytest
from langgraph.checkpoint.memory import MemorySaver

from py_hexagonal_langgraph.infrastructure.adapters.mock_llm_adapter import (
    MockLLMAdapter,
)
from py_hexagonal_langgraph.infrastructure.graph import build_graph


@pytest.fixture
def mock_llm_adapter() -> MockLLMAdapter:
    """Adapter mock con respuesta fija."""
    return MockLLMAdapter(responses=["Hola, soy el asistente"])


@pytest.fixture
def compiled_graph(mock_llm_adapter: MockLLMAdapter) -> object:
    """Grafo compilado con MockLLMAdapter. Sin llamadas a API."""
    return build_graph(
        llm_adapter=mock_llm_adapter,
        checkpointer=MemorySaver(),
    )
