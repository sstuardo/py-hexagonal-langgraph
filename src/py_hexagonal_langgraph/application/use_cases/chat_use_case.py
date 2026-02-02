"""Caso de uso: orquesta la conversación con el LLM."""

from py_hexagonal_langgraph.domain.models.agent_state import AgentState
from py_hexagonal_langgraph.domain.models.entities import DomainMessage
from py_hexagonal_langgraph.domain.ports.llm_port import LLMPort


class ChatUseCase:
    """Orquesta: recibe estado, llama al puerto LLM, devuelve actualización."""

    def __init__(
        self,
        llm_port: LLMPort,
        system_prompt: str,
    ) -> None:
        self._llm_port = llm_port
        self._system_prompt = system_prompt

    def invoke(self, state: AgentState) -> dict[str, list[DomainMessage]]:
        """Procesa el estado y devuelve las actualizaciones para messages."""
        messages = state.get("messages", [])
        if not messages:
            return {"messages": []}

        response_messages = self._llm_port.generate(
            messages=messages,
            system_prompt=self._system_prompt,
        )
        return {"messages": response_messages}
