#by taha

import logging
import httpx

from typing import Any, Dict, List, Optional
from src.config import Settings
from src.exceptions import OllamaConnectionError, OllamaException, OllamaTimeoutError

logger = logging.getLogger(__name__)


class OllamaClient:
    """Client for interacting with Ollama local LLM service."""

    def __init__(self, settings: Settings):
        """Initialize Ollama client with settings."""
        self.base_url = settings.ollama_host
        self.timeout = httpx.Timeout(30.0)

    