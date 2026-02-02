"""Servicio para cargar y gestionar prompts desacoplados."""

from __future__ import annotations

from pathlib import Path


class PromptService:
    """Carga plantillas de prompts desde archivos."""

    def __init__(self, prompts_dir: Path | None = None) -> None:
        self._prompts_dir = prompts_dir or self._default_prompts_dir()

    def _default_prompts_dir(self) -> Path:
        """Directorio por defecto: prompts/ relativo al paquete."""
        return Path(__file__).resolve().parent.parent.parent / "prompts"

    def load(self, name: str) -> str:
        """Carga un prompt por nombre (sin extensión)."""
        path = self._prompts_dir / f"{name}.txt"
        return path.read_text(encoding="utf-8").strip()
