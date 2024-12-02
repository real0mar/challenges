def evaluate_safety(report: list[int]) -> bool:

    if len(report) < 2:
        return False

    is_ascending = report[1] > report[0]
    is_descending = report[1] < report[0]

    if not is_ascending and not is_descending:
        return False

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if is_ascending and diff <= 0:
            return False
        if is_descending and diff >= 0:
            return False

    return True


if __name__ == "__main__":
    with open("advent_2024/2_input.txt") as f:
        reports = [line.strip().split() for line in f]

    safe_reports = 0
    for report in reports:
        levels = [int(num) for num in report]
        if evaluate_safety(levels):
            safe_reports += 1

    print(safe_reports)
