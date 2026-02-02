"""Protocol para persistencia. El dominio define la interfaz."""

from __future__ import annotations

from typing import Any, Protocol


class RepositoryPort(Protocol):
    """Puerto para operaciones de persistencia."""

    def save(self, key: str, value: Any) -> None:
        """Guarda un valor asociado a una clave."""
        ...

    def get(self, key: str) -> Any | None:
        """Obtiene un valor por clave. None si no existe."""
        ...
