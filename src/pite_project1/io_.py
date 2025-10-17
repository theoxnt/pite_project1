from __future__ import annotations
import os
from pathlib import Path
import json
from typing import Any
from config import Config

Record = dict[str, Any]


def load_json(path: str | Path, encoding: str = "utf-8") -> list[Record]:
    """Load a list of JSON records from *path*.

    Pure function apart from file I/O. Validates top-level type.
    """
    data = json.loads(Path(path).read_text(encoding=encoding))
    if not isinstance(data, list):
        raise ValueError("Expected a JSON list of records")
    return data


def dump_json(path: str | Path, records: list[Record], encoding: str = "utf-8") -> None:
    Path(path).write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding=encoding)

def load_config(path: str = "config.json") -> Config:
    if os.path.exists(path):
        data = json.loads(Path(path).read_text())
        return Config(
            path=data.get("pth", "data/sample.json"),
            encoding=data.get("ENC", "utf8"),
            threshold=data.get("thres", 0),
            mode=data.get("mode", "OK"),
        )
    return Config("data/sample.json", "utf8", 0, "OK")