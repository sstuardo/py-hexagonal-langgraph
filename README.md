# py-hexagonal-langgraph

Scaffold profesional en Python 3.11+ con arquitectura hexagonal, LangGraph y FastAPI.

## Estructura

- **domain/**: Modelos puros y puertos (Protocols). Sin dependencias externas.
- **application/**: Casos de uso y servicios compartidos.
- **infrastructure/**: LangGraph, adapters (OpenAI, Postgres), API FastAPI, configuración.

## Instalación

```bash
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

O con pip:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Configuración

Copiar `.env.example` a `.env` y configurar las variables.

## Ejecución

```bash
uvicorn py_hexagonal_langgraph.infrastructure.api.app:app --reload
```

## Calidad

```bash
ruff check src tests
ruff format src tests --check
mypy src
pytest tests -v
```
