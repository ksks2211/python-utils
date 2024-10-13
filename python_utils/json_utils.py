import json
from typing import Any, Mapping

from .file_utils import write_file


def to_json(data):
    return json.dumps(data, indent=4)


def save_dict_as_json(data: Mapping[str, Any], location: str) -> None:
    json = to_json(data)
    write_file(content=json, file_path=location)
