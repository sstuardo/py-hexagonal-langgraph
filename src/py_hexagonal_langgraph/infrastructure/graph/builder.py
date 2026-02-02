"""Construye el StateGraph de LangGraph con nodos y aristas."""

from typing import TYPE_CHECKING

from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from py_hexagonal_langgraph.application.services.prompt_service import (
    PromptService,
)
from py_hexagonal_langgraph.application.use_cases.chat_use_case import (
    ChatUseCase,
)
from py_hexagonal_langgraph.domain.ports.llm_port import LLMPort
from py_hexagonal_langgraph.infrastructure.graph.nodes import (
    GraphState,
    create_agent_node,
)

if TYPE_CHECKING:
    from langgraph.checkpoint.base import BaseCheckpointSaver


def build_graph(
    llm_adapter: LLMPort,
    prompt_name: str = "system_prompt",
    checkpointer: "BaseCheckpointSaver | None" = None,
) -> CompiledStateGraph:
    """Construye y compila el grafo con el adaptador LLM inyectado."""
    prompt_service = PromptService()
    system_prompt = prompt_service.load(prompt_name)

    chat_use_case = ChatUseCase(
        llm_port=llm_adapter,
        system_prompt=system_prompt,
    )

    graph = StateGraph(GraphState)
    graph.add_node("agent", create_agent_node(chat_use_case))
    graph.add_edge(START, "agent")
    graph.add_edge("agent", END)

    return graph.compile(checkpointer=checkpointer)
