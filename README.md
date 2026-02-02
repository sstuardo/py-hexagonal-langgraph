# py-hexagonal-langgraph

> Scaffold profesional en Python 3.11+ para construir agentes de IA con arquitectura hexagonal, LangGraph y FastAPI.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/sstuardo/py-hexagonal-langgraph/actions/workflows/ci.yml/badge.svg)](https://github.com/sstuardo/py-hexagonal-langgraph/actions/workflows/ci.yml)

## Por qué este scaffold

- **Arquitectura hexagonal**: Dominio puro sin dependencias externas, fácil de testear y extender.
- **LangGraph**: Grafo de estado con `AgentState`, listo para agentes conversacionales.
- **Inyección de dependencias**: Cambia OpenAI por otro LLM sin tocar el dominio.
- **Calidad integrada**: Ruff, Mypy y Pytest configurados desde el inicio.

## Quick Start

```bash
# 1. Clonar e instalar
git clone https://github.com/sstuardo/py-hexagonal-langgraph.git
cd py-hexagonal-langgraph
pip install -e ".[dev]"

# 2. Configurar (copiar .env.example a .env y añadir OPENAI_API_KEY)
cp .env.example .env

# 3. Ejecutar
uvicorn py_hexagonal_langgraph.infrastructure.api.app:app --reload

# 4. Probar
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" \
  -d '{"message": "Hola", "thread_id": "test"}'
```

## Arquitectura

El flujo sigue el patrón hexagonal: los nodos de LangGraph invocan casos de uso que usan puertos (Protocols). Los adaptadores concretos (OpenAI, Mock) se inyectan en tiempo de construcción.

Ver el [PLAN.md](PLAN.md) para el diagrama completo y la arquitectura detallada.

## Estructura del proyecto

```
src/py_hexagonal_langgraph/
├── domain/          # Modelos puros y puertos (Protocols)
├── application/     # Casos de uso y servicios
└── infrastructure/  # LangGraph, adapters, API FastAPI, config
```

## Características

- **Dominio puro**: `DomainMessage`, `AgentState` con `Annotated` y `operator.add`.
- **Puertos**: `LLMPort` y `RepositoryPort` para desacoplar infraestructura.
- **LangGraph**: Grafo compilado con checkpointer para conversaciones con historial.
- **FastAPI**: Endpoints `/chat` y `/health` con schemas Pydantic.
- **Tests**: Unitarios (dominio, aplicación) e integración (grafo, API) con `MockLLMAdapter`.

## Uso

### Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/chat` | Envía un mensaje y recibe la respuesta del asistente. |
| GET | `/health` | Health check. |

### Ejemplo de chat

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "¿Qué puedes hacer?", "thread_id": "mi-sesion"}'
```

## Desarrollo

```bash
# Lint
ruff check src tests

# Formato
ruff format src tests --check

# Tipos
mypy src

# Tests
pytest tests -v
```

## Licencia

[MIT](LICENSE)
