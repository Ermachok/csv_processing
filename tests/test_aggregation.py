import pytest

from csv_processor.core.aggregation import get_aggregator


@pytest.mark.parametrize(
    "operation,expected",
    [
        ("min", 1),
        ("max", 4),
        ("avg", (1 + 2 + 3 + 4) / 4),
    ],
)
def test_aggregate_rating(sample_data, operation, expected):
    aggregator = get_aggregator(operation)
    result = aggregator.aggregate(sample_data, "rating")
    assert result == pytest.approx(expected, rel=1e-3)


@pytest.mark.parametrize("operation", ["min", "max", "avg"])
def test_aggregate_raises_on_non_numeric_column(sample_data, operation):
    aggregator = get_aggregator(operation)
    with pytest.raises(ValueError):
        aggregator.aggregate(sample_data, "name")
