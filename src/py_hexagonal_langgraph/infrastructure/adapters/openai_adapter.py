"""Adapter que implementa LLMPort con OpenAI."""

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage

from py_hexagonal_langgraph.domain.models.entities import DomainMessage


def _to_base_message(msg: DomainMessage) -> BaseMessage:
    """Convierte DomainMessage a BaseMessage de LangChain."""
    if msg.role == "human":
        return HumanMessage(content=msg.content)
    if msg.role == "ai":
        return AIMessage(content=msg.content)
    return SystemMessage(content=msg.content)


def _to_domain_message(msg: BaseMessage) -> DomainMessage:
    """Convierte BaseMessage a DomainMessage."""
    role: str = getattr(msg, "type", "ai")
    if role == "human":
        return DomainMessage(role="human", content=msg.content)
    return DomainMessage(role="ai", content=msg.content)


class OpenAIAdapter:
    """Implementa LLMPort usando OpenAI vía LangChain."""

    def __init__(self, api_key: str, model: str = "gpt-4o-mini") -> None:
        self._api_key = api_key
        self._model = model

    def generate(
        self,
        messages: list[DomainMessage],
        system_prompt: str,
    ) -> list[DomainMessage]:
        """Genera respuesta usando OpenAI."""
        from langchain_openai import ChatOpenAI

        llm = ChatOpenAI(
            api_key=self._api_key,
            model=self._model,
            temperature=0.7,
        )
        lc_messages: list[BaseMessage] = [
            SystemMessage(content=system_prompt),
            *[_to_base_message(m) for m in messages],
        ]
        response = llm.invoke(lc_messages)
        return [_to_domain_message(response)]
