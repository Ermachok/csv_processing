import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="CSV Processor")
    parser.add_argument("--file", required=True, help="Path to the CSV file")

    parser.add_argument(
        "--where", help="Filter condition, e.g. 'price>500' or 'brand=xiaomi'"
    )

    parser.add_argument(
        "--aggregate",
        nargs=2,
        metavar=("COLUMN", "OPERATION"),
        help="Aggregation like: --aggregate price avg",
    )

    return parser.parse_args()
