import pytest

from csv_processor.core.filter import apply_filter


@pytest.mark.parametrize(
    "condition,expected_names",
    [
        ("price>150", ["galaxy", "redmi", "poco"]),
        ("price<300", ["iphone", "galaxy"]),
        ("brand=xiaomi", ["redmi", "poco"]),
        ("name=iphone", ["iphone"]),
    ],
)
def test_apply_filter(condition, expected_names, sample_data):
    result = apply_filter(sample_data, condition)
    names = [row["name"] for row in result]
    assert sorted(names) == sorted(expected_names)
