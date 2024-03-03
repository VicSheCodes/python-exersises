import os
from dataclasses import dataclass
from typing import Tuple


@dataclass
class CeleryConfig:
    broker_url: str = "redis://localhost:6380/0"
    database_url: str = (
        "postgresql+psycopg2://postgres:postgres@localhost:5430/postgres"
    )
    task_default_queue: str = "default"
    imports: Tuple[str] = ("tasks",)
