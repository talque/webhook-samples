from typing import Any
import json


def pretty_print(data: dict[str, Any]):
    encoded = json.dumps(data, indent=4, sort_keys=True)
    print(encoded)
