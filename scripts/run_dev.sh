#!/usr/bin/env bash
# Ejecuta uvicorn en modo desarrollo
exec uvicorn py_hexagonal_langgraph.infrastructure.api.app:app --reload
