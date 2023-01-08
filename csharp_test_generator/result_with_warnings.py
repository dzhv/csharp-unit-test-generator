from typing import Generic, TypeVar, List

T = TypeVar("T")

class ResultWithWarnings(Generic[T]):
    def __init__(self, result: T, warnings: List[str]):
        self.warnings: List[str] = warnings
        self.result: T = result
