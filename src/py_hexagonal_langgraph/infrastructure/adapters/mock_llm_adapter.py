"""Adapter mock que implementa LLMPort para tests. Sin llamadas a API."""

from __future__ import annotations

from py_hexagonal_langgraph.domain.models.entities import DomainMessage


class MockLLMAdapter:
    """Implementa LLMPort con respuestas fijas. Para tests sin consumir tokens."""

    def __init__(self, responses: list[str] | None = None) -> None:
        self._responses = responses or ["respuesta de prueba"]
        self._call_index = 0

    def generate(
        self,
        messages: list[DomainMessage],
        system_prompt: str,
    ) -> list[DomainMessage]:
        """Devuelve la siguiente respuesta configurada."""
        response = self._responses[self._call_index % len(self._responses)]
        self._call_index += 1
        return [DomainMessage(role="ai", content=response)]
