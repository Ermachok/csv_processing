from tabulate import tabulate

def print_table(rows: list[dict]) -> None:
    print(tabulate(rows, headers="keys"))
