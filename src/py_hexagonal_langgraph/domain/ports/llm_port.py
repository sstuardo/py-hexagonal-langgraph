"""Protocol para invocar LLMs. El dominio define la interfaz."""

from typing import Protocol

from py_hexagonal_langgraph.domain.models.entities import DomainMessage


class LLMPort(Protocol):
    """Puerto para generar respuestas con un modelo de lenguaje."""

    def generate(
        self,
        messages: list[DomainMessage],
        system_prompt: str,
    ) -> list[DomainMessage]:
        """Genera mensajes de respuesta dado el historial y el prompt de sistema."""
        ...
