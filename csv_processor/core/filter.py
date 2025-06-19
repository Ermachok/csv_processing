import operator
from typing import Callable


def apply_filter(rows: list[dict], condition: str) -> list[dict]:
    ops: dict[str, Callable[[any, any], bool]] = {
        "=": operator.eq,
        ">": operator.gt,
        "<": operator.lt,
    }

    for op_str in ops:
        if op_str in condition:
            key, val = condition.split(op_str, 1)
            key, val = key.strip(), val.strip()
            compare = ops[op_str]
            return [row for row in rows if compare(cast(row[key]), cast(val))]

    raise ValueError(f"Неподдерживаемое условие фильтрации: {condition}")


def cast(value: str) -> float | str:
    try:
        return float(value)
    except ValueError:
        return value
