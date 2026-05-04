import argparse
from collections import Counter
from typing import List, Dict


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Парсить один рядок лог-файлу у словник.

    Очікуваний формат:
    DATE TIME LEVEL MESSAGE
    """
    parts = line.split(maxsplit=3)

    if len(parts) < 4:
        raise ValueError("Невірний формат лог-рядка")

    date, time, level, message = parts

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message,
    }


def load_logs(file_path: str) -> List[Dict[str, str]]:
    """Зчитує лог-файл і повертає список логів."""
    with open(file_path, "r", encoding="utf-8") as file:
        return [parse_log_line(line) for line in file]


def filter_logs_by_level(
    logs: List[Dict[str, str]], level: str
) -> List[Dict[str, str]]:
    """Фільтрує логи за рівнем."""
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(
        logs: List[Dict[str, str]]
) -> Dict[str, int]:
    """Підраховує кількість логів по рівнях."""
    return dict(Counter(log["level"] for log in logs))


def display_log_counts(counts: Dict[str, int]) -> None:
    """Виводить таблицю кількості логів по рівнях."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def display_logs_by_level(
    logs: List[Dict[str, str]], level: str
) -> None:
    """Виводить деталі логів для заданого рівня."""
    if not logs:
        print(f"\nНемає логів для рівня '{level}'")
        return

    print(f"\nДеталі логів для рівня '{level}':")

    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message'].strip()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Парсер логів")
    parser.add_argument("file", help="Шлях до лог-файлу")
    parser.add_argument(
        "level",nargs="?", default=None,
        help="Фільтр рівня логів (наприклад: INFO, ERROR)",
    )

    args = parser.parse_args()

    logs = load_logs(args.file)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if args.level:
        level = args.level.upper()
        filtered_logs = filter_logs_by_level(logs, level)
        display_logs_by_level(filtered_logs, level)


if __name__ == "__main__":
    main()