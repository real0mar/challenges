def evaluate_safety(report: list[int]) -> bool:
    if len(report) < 2:
        return False

    is_ascending = all(report[i] > report[i - 1] for i in range(1, len(report)))
    is_descending = all(report[i] < report[i - 1] for i in range(1, len(report)))

    if not (is_ascending or is_descending):
        return False

    return all(1 <= abs(report[i] - report[i - 1]) <= 3 for i in range(1, len(report)))


def evaluate_safety_dampener(report: list[int]) -> bool:
    return evaluate_safety(report) or any(
        evaluate_safety(report[:i] + report[i + 1 :]) for i in range(len(report))
    )


if __name__ == "__main__":
    with open("advent_2024/2_input.txt") as f:
        reports = [[int(num) for num in line.strip().split()] for line in f]

    safe_reports = sum(evaluate_safety(report) for report in reports)
    print(safe_reports)

    safe_reports_dampener = sum(evaluate_safety_dampener(report) for report in reports)
    print(safe_reports_dampener)
