import csv


def load_csv(file_path: str) -> list[dict]:
    with open(file_path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
