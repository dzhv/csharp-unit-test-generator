from typing import Generic, TypeVar, List

T = TypeVar("T")

class ResultWithWarnings(Generic[T]):
    def __init__(self):
        self.warnings: List[str] = []

    
