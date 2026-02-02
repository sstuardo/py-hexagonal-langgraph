"""Adapter que implementa RepositoryPort con PostgreSQL."""


class PostgresRepository:
    """Implementa RepositoryPort usando PostgreSQL. Placeholder para conexión real."""

    def __init__(self, database_url: str) -> None:
        self._database_url = database_url
        self._store: dict[str, object] = {}  # Placeholder hasta conectar

    def save(self, key: str, value: object) -> None:
        """Guarda un valor. Placeholder: usa dict en memoria."""
        self._store[key] = value

    def get(self, key: str) -> object | None:
        """Obtiene un valor. Placeholder: usa dict en memoria."""
        return self._store.get(key)
