def evaluate_safety(report: list[int]) -> bool:
    """The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three."""

    is_ascending: bool = report[1] > report[0]
    if is_ascending:
        for i in range(1, len(report)):
            if report[i] - report[i-1] > 3:
                return False
    else:
        for i in range(1, len(report)):
            if report[i] - report[i-1] < -3:
                return False
    return True

if __name__ == "__main__":
    with open("advent_2024/2_input.txt") as f:
        reports = [line.strip().split() for line in f]
    
    # get the number of safe reports

    safe_reports: int = 0
    for report in reports:
        if evaluate_safety([int(num) for num in report]):
            safe_reports += 1

    print(safe_reports)