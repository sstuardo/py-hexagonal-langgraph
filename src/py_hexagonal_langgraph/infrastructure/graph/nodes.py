"""Nodos del grafo que invocan casos de uso."""

from __future__ import annotations

import operator
from typing import TYPE_CHECKING, Annotated, TypedDict

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage

from py_hexagonal_langgraph.application.use_cases.chat_use_case import (
    ChatUseCase,
)
from py_hexagonal_langgraph.domain.models.entities import DomainMessage

if TYPE_CHECKING:
    from py_hexagonal_langgraph.domain.models.agent_state import AgentState


class GraphState(TypedDict, total=False):
    """Estado del grafo LangGraph. Usa BaseMessage para compatibilidad."""

    messages: Annotated[list[BaseMessage], operator.add]


def _to_domain_message(msg: BaseMessage) -> DomainMessage:
    """Convierte BaseMessage a DomainMessage."""
    msg_type = getattr(msg, "type", "ai")
    role: str = "human" if msg_type == "human" else "ai"
    return DomainMessage(role=role, content=msg.content)


def _to_base_message(msg: DomainMessage) -> BaseMessage:
    """Convierte DomainMessage a BaseMessage."""
    if msg.role == "human":
        return HumanMessage(content=msg.content)
    return AIMessage(content=msg.content)


def create_agent_node(chat_use_case: ChatUseCase) -> object:
    """Factory que devuelve el nodo del agente con el use case inyectado."""

    def agent_node(state: GraphState) -> dict[str, list[BaseMessage]]:
        # Convertir GraphState a AgentState (dominio)
        domain_messages = [_to_domain_message(m) for m in state.get("messages", [])]
        domain_state: AgentState = {"messages": domain_messages}

        # Invocar caso de uso
        updates = chat_use_case.invoke(domain_state)

        # Convertir respuesta a BaseMessage para LangGraph
        base_messages = [_to_base_message(m) for m in updates.get("messages", [])]
        return {"messages": base_messages}

    return agent_node
