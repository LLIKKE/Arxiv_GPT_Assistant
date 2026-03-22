import dataclasses
import json
from typing import TypeVar, List

T = TypeVar("T")

class EnhancedJSONEncoder(json.JSONEncoder):
    """
    A custom JSON encoder that supports encoding dataclasses.
    """
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

def batched(items: List[T], batch_size: int) -> List[List[T]]:
    """
    Takes a list and returns a list of lists, each of size `batch_size`.
    """
    return [items[i : i + batch_size] for i in range(0, len(items), batch_size)]

def argsort(seq) -> List[int]:
    """
    Native Python version of an 'argsort'.
    Returns a list of indices that would sort the array.
    """
    return sorted(range(len(seq)), key=seq.__getitem__)
