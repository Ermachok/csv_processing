from .base import Aggregator


class MinAggregator(Aggregator):
    def aggregate(self, rows, column):
        return min(float(row[column]) for row in rows)


class MaxAggregator(Aggregator):
    def aggregate(self, rows, column):
        return max(float(row[column]) for row in rows)


class AvgAggregator(Aggregator):
    def aggregate(self, rows, column):
        values = [float(row[column]) for row in rows]
        return sum(values) / len(values)


def get_aggregator(op: str) -> Aggregator:
    if op == "min":
        return MinAggregator()
    if op == "max":
        return MaxAggregator()
    if op == "avg":
        return AvgAggregator()
    raise ValueError(f"Unsupported aggregation operation: {op}")
