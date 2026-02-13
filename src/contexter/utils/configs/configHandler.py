from dataclasses import dataclass


@dataclass
class ProviderConfig:
    provider_name: str = "anthrophic"


@dataclass
class ContexterConfig:
    debug: bool = False
    memorize: bool = False
    enable_cache: bool = False
    vector_db: str = "chromadb"
