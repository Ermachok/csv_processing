from csv_processor.cli import parse_args
from csv_processor.core.aggregation import get_aggregator
from csv_processor.core.filter import apply_filter
from csv_processor.core.loader import load_csv
from csv_processor.utils.logger import logger
from csv_processor.utils.printer import print_table
from csv_processor.utils.validation import (
    ensure_column_exists,
    ensure_column_is_numeric,
)

VALID_AGG_OPS = {"min", "max", "avg"}


def main():
    args = parse_args()
    logger.debug("Старт скрипта с аргументами: %s", args)

    try:
        rows = load_csv(args.file)
        logger.info("CSV-файл '%s' успешно загружен (%d строк)", args.file, len(rows))

        if args.where:
            col = args.where.split("=")[0].split(">")[0].split("<")[0].strip()
            ensure_column_exists(rows, col)
            logger.info("Применяем фильтр: %s", args.where)
            rows = apply_filter(rows, args.where)

        if args.aggregate:
            col, op = args.aggregate
            ensure_column_exists(rows, col)
            ensure_column_is_numeric(rows, col)

            if op not in VALID_AGG_OPS:
                logger.error("Недопустимая операция агрегации: %s", op)
                raise ValueError(
                    f"Недопустимая операция агрегации '{op}'."
                    f"Допустимые: {', '.join(VALID_AGG_OPS)}"
                )

            logger.info("Агрегация: %s по колонке '%s'", op, col)
            aggregator = get_aggregator(op)
            result = aggregator.aggregate(rows, col)
            print(f"{op}({col}) = {result}")
        else:
            print_table(rows)

    except Exception as e:
        logger.error("Ошибка при выполнении скрипта: %s", e)
        raise


if __name__ == "__main__":
    main()
