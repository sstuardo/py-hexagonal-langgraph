"""Entidades puras del dominio. Sin dependencias externas."""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class DomainMessage:
    """Mensaje del dominio. role + content."""

    role: Literal["human", "ai", "system"]
    content: str


@dataclass(frozen=True)
class ToolResult:
    """Resultado de una herramienta invocada por el agente."""

    tool_name: str
    result: str
