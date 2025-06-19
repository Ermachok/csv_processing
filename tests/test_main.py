import os
import subprocess
import tempfile
import textwrap

import pytest

CSV_CONTENT = textwrap.dedent(
    """\
    name,brand,price,rating
    iphone,apple,999,4.9
    galaxy,samsung,1199,4.8
"""
)


@pytest.fixture
def temp_csv_file():
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".csv") as f:
        f.write(CSV_CONTENT)
        f.flush()
        yield f.name
    os.remove(f.name)


def run_main(args):
    return subprocess.run(
        ["python", "-m", "csv_processor.main"] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )


def test_main_runs_filter(temp_csv_file):
    result = run_main(["--file", temp_csv_file, "--where", "price>1000"])
    assert "galaxy" in result.stdout
    assert "iphone" not in result.stdout


def test_main_runs_aggregate(temp_csv_file):
    result = run_main(["--file", temp_csv_file, "--aggregate", "price", "avg"])
    assert "avg(price)" in result.stdout
    assert "1099.0" in result.stdout


def test_main_invalid_file():
    result = run_main(["--file", "nonexistent.csv"])
    assert result.returncode != 0
    assert "Ошибка" in result.stderr or "No such file" in result.stderr
