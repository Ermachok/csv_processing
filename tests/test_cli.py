import sys

import pytest

from csv_processor import cli


def test_parse_args_minimal(monkeypatch):
    testargs = ["prog", "--file", "data.csv"]
    monkeypatch.setattr(sys, "argv", testargs)
    args = cli.parse_args()
    assert args.file == "data.csv"
    assert args.where is None
    assert args.aggregate is None


def test_parse_args_with_where(monkeypatch):
    testargs = ["prog", "--file", "data.csv", "--where", "price>100"]
    monkeypatch.setattr(sys, "argv", testargs)
    args = cli.parse_args()
    assert args.where == "price>100"


def test_parse_args_with_aggregate(monkeypatch):
    testargs = ["prog", "--file", "data.csv", "--aggregate", "price", "avg"]
    monkeypatch.setattr(sys, "argv", testargs)
    args = cli.parse_args()
    assert args.aggregate == ["price", "avg"]


def test_parse_args_missing_file(monkeypatch):
    testargs = ["prog"]
    monkeypatch.setattr(sys, "argv", testargs)
    with pytest.raises(SystemExit):
        cli.parse_args()
