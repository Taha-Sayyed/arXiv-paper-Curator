#by taha
import time
from functools import cached_property
from pathlib import Path
from typing import Dict, List, Optional
from src.config import ArxivSettings

class ArxivClient:
    """Client for fetching papers from arXiv API"""
    def __init__(self,settings:ArxivSettings):
        self.__settings=settings
        #To track the time when client made last request for Rate limitting
        self._last_request_time:Optional[float]=None

    @cached_property
    def pdf_cache_dir(self)->Path:
        cache_dir=Path()