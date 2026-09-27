"""Student-facing configuration helpers for Lab 02."""

from __future__ import annotations

import os


def load_config() -> dict:
    """
    Load configuration from environment variables.

    Expected keys:
    - LLM_PROVIDER
    - OPENAI_API_KEY
    - OPENAI_MODEL
    """
    return {
        "LLM_PROVIDER": os.environ.get("LLM_PROVIDER", "mock"),
        "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY", ""),
        "OPENAI_MODEL": os.environ.get("OPENAI_MODEL", ""),
    }
