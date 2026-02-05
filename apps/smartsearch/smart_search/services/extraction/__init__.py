"""
Extraction Module

Provides content extraction from various file types using pluggable strategies.
"""

from smart_search.services.extraction.basic_strategy import BasicExtractionStrategy
from smart_search.services.extraction.extractor import ContentExtractor, get_extractor
from smart_search.services.extraction.protocol import ExtractionStrategy
from smart_search.services.extraction.tika_strategy import TikaExtractionStrategy

__all__ = [
    "ExtractionStrategy",
    "TikaExtractionStrategy",
    "BasicExtractionStrategy",
    "ContentExtractor",
    "get_extractor",
]
