"""AgentState para LangGraph. Usa Annotated + operator.add para el historial."""

import operator
from typing import Annotated, TypedDict

from py_hexagonal_langgraph.domain.models.entities import DomainMessage


class AgentState(TypedDict, total=False):
    """Estado del agente. messages usa operator.add para acumular."""

    messages: Annotated[list[DomainMessage], operator.add]
