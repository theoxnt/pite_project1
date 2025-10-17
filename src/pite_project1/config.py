from dataclasses import dataclass 

@dataclass(frozen=True)
class Config:
    path: str
    encoding: str
    threshold: int
    mode: str
