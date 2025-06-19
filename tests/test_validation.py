import pytest

from csv_processor.utils import validation


@pytest.fixture
def non_numeric_data():
    return [
        {"name": "iphone", "brand": "apple", "price": "100", "rating": "1"},
        {"name": "galaxy", "brand": "samsung", "price": "abc", "rating": "2"},
    ]


def test_ensure_column_exists_ok(sample_data):
    validation.ensure_column_exists(sample_data, "price")


def test_ensure_column_exists_empty_rows():
    with pytest.raises(ValueError, match="CSV-файл пуст"):
        validation.ensure_column_exists([], "price")


def test_ensure_column_exists_missing_column(sample_data):
    with pytest.raises(ValueError, match="отсутствует в CSV"):
        validation.ensure_column_exists(sample_data, "nonexistent")


def test_ensure_column_is_numeric_ok(sample_data):
    validation.ensure_column_is_numeric(sample_data, "price")


def test_ensure_column_is_numeric_fail(non_numeric_data):
    with pytest.raises(ValueError, match="не является числом"):
        validation.ensure_column_is_numeric(non_numeric_data, "price")
