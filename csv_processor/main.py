from csv_processor.cli import parse_args
from csv_processor.core.loader import load_csv
from csv_processor.core.filter import apply_filter
from csv_processor.core.aggregation import get_aggregator
from csv_processor.utils.printer import print_table
from csv_processor.utils.validation import ensure_column_exists, ensure_column_is_numeric


VALID_AGG_OPS = {"min", "max", "avg"}

def main():
    args = parse_args()
    rows = load_csv(args.file)

    if args.filter:
        col = args.filter.split("=")[0].split(">")[0].split("<")[0].strip()
        ensure_column_exists(rows, col)
        rows = apply_filter(rows, args.filter)

    if args.agg:
        col, op = args.agg
        if op not in VALID_AGG_OPS:
            raise ValueError(f"Недопустимая агрегация: {op}")
        ensure_column_exists(rows, col)
        ensure_column_is_numeric(rows, col)
        aggregator = get_aggregator(op)
        result = aggregator.aggregate(rows, col)
        print(f"{op}({col}) = {result}")
    else:
        print_table(rows)


if __name__ == "__main__":
    main()
