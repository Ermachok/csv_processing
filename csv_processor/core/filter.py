from typing import Callable

def apply_filter(rows: list[dict], condition: str) -> list[dict]:
    import operator

    ops: dict[str, Callable] = {
        "=": operator.eq,
        ">": operator.gt,
        "<": operator.lt,
    }

    for op_str, func in ops.items():
        if op_str in condition:
            key, val = condition.split(op_str)
            key, val = key.strip(), val.strip()
            return [row for row in rows if func(cast(row[key]), cast(val))]

    raise ValueError(f"Invalid filter: {condition}")

def cast(value: str):
    try:
        return float(value)
    except ValueError:
        return value
