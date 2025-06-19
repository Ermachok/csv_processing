def ensure_column_exists(rows: list[dict], column: str):
    if not rows:
        raise ValueError("CSV-файл пуст.")
    if column not in rows[0]:
        raise ValueError(f"Указанный столбец '{column}' отсутствует в CSV.")


def ensure_column_is_numeric(rows: list[dict], column: str):
    for row in rows:
        try:
            float(row[column])
        except ValueError:
            raise ValueError(
                f"Значение в колонке '{column}' не является числом: {row[column]}"
            )
