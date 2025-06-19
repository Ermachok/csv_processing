from abc import ABC, abstractmethod


class Aggregator(ABC):
    @abstractmethod
    def aggregate(self, rows: list[dict], column: str) -> float:
        pass
