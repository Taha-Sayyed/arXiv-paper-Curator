#by Taha
from typing import List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class DefaultSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        frozen=True,
        env_nested_delimiter="__",
    )


class ArxivSettings(DefaultSettings):
    """arXiv API client settings."""

    base_url: str = "https://export.arxiv.org/api/query"
    namespaces: dict = Field(
        default={
            "atom": "http://www.w3.org/2005/Atom",
            "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
            "arxiv": "http://arxiv.org/schemas/atom",
        }
    )
    pdf_cache_dir: str = "./data/arxiv_pdfs"
    rate_limit_delay: float = 3.0  # seconds between requests
    timeout_seconds: int = 30
    max_results: int = 100
    search_category: str = "cs.AI"  # Default category to search

class Settings(DefaultSettings):
    # arXiv settings
    arxiv: ArxivSettings = Field(default_factory=ArxivSettings)

    ## Ollama configuration
    ollama_host: str = "http://localhost:11434"
    ollama_models: List[str] = Field(default=["llama3.2:1b"])
    ollama_default_model: str = "llama3.2:1b"
    ollama_timeout: int = 300  # 5 minutes for LLM operations

    @field_validator("ollama_models", mode="before")
    @classmethod
    def parse_ollama_models(cls, v):
        """Parse comma-separated string into list of models."""
        if isinstance(v, str):
            return [model.strip() for model in v.split(",") if model.strip()]
        return v



def get_settings() -> Settings:
    """Get application settings."""
    return Settings()