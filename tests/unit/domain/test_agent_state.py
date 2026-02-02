"""Tests del AgentState y merge con operator.add."""

import operator
from typing import Annotated, TypedDict

import pytest

from py_hexagonal_langgraph.domain.models.entities import DomainMessage


class AgentState(TypedDict, total=False):
    """Réplica del AgentState para probar la semántica de merge."""

    messages: Annotated[list[DomainMessage], operator.add]


def test_operator_add_accumulates_messages() -> None:
    """operator.add concatena listas en lugar de reemplazar."""
    reducer = operator.add
    existing: list[DomainMessage] = [
        DomainMessage(role="human", content="Hola"),
        DomainMessage(role="ai", content="Hola!"),
    ]
    new: list[DomainMessage] = [
        DomainMessage(role="human", content="¿Cómo estás?"),
    ]
    result = reducer(existing, new)
    assert len(result) == 3
    assert result[0].content == "Hola"
    assert result[2].content == "¿Cómo estás?"


def test_domain_message_immutable() -> None:
    """DomainMessage es frozen (inmutable)."""
    msg = DomainMessage(role="human", content="test")
    with pytest.raises(AttributeError):
        msg.content = "modified"  # type: ignore[misc]
