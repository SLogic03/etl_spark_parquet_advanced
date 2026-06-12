"""Utilidades compartidas del proyecto."""

from pathlib import Path


def project_root() -> Path:
    """Devuelve la ruta base del proyecto."""
    return Path(__file__).resolve().parent.parent
