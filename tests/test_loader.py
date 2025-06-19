import os
import tempfile

import pytest

from csv_processor.core.loader import load_csv

CSV_CONTENT = """name,brand,price,rating
iphone,apple,999,4.9
galaxy,samsung,1199,4.8
"""


def test_load_csv_reads_file_correctly():
    with tempfile.NamedTemporaryFile(
        "w+", delete=False, encoding="utf-8", suffix=".csv"
    ) as f:
        f.write(CSV_CONTENT)
        tmp_path = f.name

    try:
        rows = load_csv(tmp_path)
        assert isinstance(rows, list)
        assert len(rows) == 2
        assert rows[0]["name"] == "iphone"
        assert rows[1]["brand"] == "samsung"
    finally:
        os.remove(tmp_path)


def test_load_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv("non_existent_file.csv")
