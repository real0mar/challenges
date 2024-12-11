from pathlib import Path

EXAMPLE = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

REAL_IN = Path("advent_2024/7_input.txt").read_text()


def evaluate_truth(expression: str, concat=False) -> int:
    """Evaluates whether a given expression can achieve a target value using a combination of addition and multiplication.
    The expression is a string formatted as "target:n1 n2 n3 ...", where "target" is the integer value to achieve,
    and "n1 n2 n3 ..." are the integers that can be used in the operations.
    The function uses a helper function to recursively check if the target can be achieved by either adding or multiplying
    the numbers in the given order.

    Args:
        expression (str): The input string containing the target and the list of numbers.

    Returns:
        int: The target value if it can be achieved, otherwise 0.

    """
    if not expression:
        return 0
    split = expression.split(":")
    target = int(split[0])
    numbers = list(map(int, split[1].split()))

    def helper(index, current_value):
        if index == len(numbers):
            return current_value == target

        if not concat:
            return helper(index + 1, current_value + numbers[index]) or helper(
                index + 1, current_value * numbers[index]
            )

        return helper(index + 1, current_value * numbers[index]) or helper(
            index + 1,
            current_value + numbers[index]
            or helper(index + 1, int(str(current_value) + str(numbers[index]))),
        )

    if helper(1, numbers[0]):
        return target
    return 0


def part1(input: str) -> int:
    return sum(evaluate_truth(expression) for expression in input.split("\n"))


def part2(input: str) -> int:
    return sum(
        evaluate_truth(expression, concat=True) for expression in input.split("\n")
    )


if __name__ == "__main__":
    assert part1(EXAMPLE) == 3749
    assert part2(EXAMPLE) == 11387

    print(part1(REAL_IN))
    print(part2(REAL_IN))
