import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="CSV Processor")
    parser.add_argument("--file", required=True, help="Path to the CSV file")

    parser.add_argument(
        "--filter",
        help="Filter condition, e.g. 'price>500' or 'brand=xiaomi'"
    )

    parser.add_argument(
        "--agg",
        nargs=2,
        metavar=('COLUMN', 'OPERATION'),
        help="Aggregation like: --agg price avg"
    )

    return parser.parse_args()
