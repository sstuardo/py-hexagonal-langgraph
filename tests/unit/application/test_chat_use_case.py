"""Tests del ChatUseCase con MockLLMAdapter."""

from __future__ import annotations

from typing import TYPE_CHECKING

from py_hexagonal_langgraph.application.use_cases.chat_use_case import (
    ChatUseCase,
)
from py_hexagonal_langgraph.domain.models.entities import DomainMessage

if TYPE_CHECKING:
    from py_hexagonal_langgraph.domain.models.agent_state import AgentState
from py_hexagonal_langgraph.infrastructure.adapters.mock_llm_adapter import (
    MockLLMAdapter,
)


def test_chat_use_case_returns_llm_response() -> None:
    """El use case devuelve la respuesta del puerto LLM."""
    mock_llm = MockLLMAdapter(responses=["Respuesta fija"])
    use_case = ChatUseCase(llm_port=mock_llm, system_prompt="Eres útil.")

    state: AgentState = {
        "messages": [DomainMessage(role="human", content="Hola")],
    }
    result = use_case.invoke(state)

    assert "messages" in result
    assert len(result["messages"]) == 1
    assert result["messages"][0].role == "ai"
    assert result["messages"][0].content == "Respuesta fija"


def test_chat_use_case_empty_messages_returns_empty() -> None:
    """Con mensajes vacíos devuelve lista vacía."""
    mock_llm = MockLLMAdapter()
    use_case = ChatUseCase(llm_port=mock_llm, system_prompt="")

    state: AgentState = {"messages": []}
    result = use_case.invoke(state)

    assert result["messages"] == []
