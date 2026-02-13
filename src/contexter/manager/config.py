from dataclasses import dataclass, field, asdict
import os
from typing import Optional
import json
from contexter.utils.configs.configHandler import ProviderConfig, ContexterConfig


@dataclass
class ProjectConfig:
    name: Optional[str] = field(default_factory=lambda: os.getcwd().split("/")[-1])
    provider: ProviderConfig = field(default_factory=ProviderConfig)
    contexter: ContexterConfig = field(default_factory=ContexterConfig)


def initialize_project(provider_name: Optional[str]):
    proj_config = ProjectConfig()

    if provider_name:
        proj_config.provider.provider_name = provider_name

    config_path = os.path.join(os.getcwd(), "config.json")

    with open(config_path, "w") as f:
        json.dump(asdict(proj_config), f, indent=2)
