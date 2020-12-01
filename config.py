from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    database_uri: str = 'sqlite:///app.db'