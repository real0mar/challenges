from collections import defaultdict

real_input = [
    int(x) for x in ["6571", "0", "5851763", "526746", "23", "69822", "9", "989"]
]
example_input = [int(x) for x in ["0", "1", "10", "99", "999"]]
example_output = [int(x) for x in ["1", "2024", "1", "0", "9", "9", "2021976"]]


def blink(wall: list[int]) -> list[int]:
    blinked: list[int] = []
    for stone in wall:
        if stone == 0:
            blinked.append(1)
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            mid = len(str_stone) // 2
            blinked.append(int(str(stone)[:mid]))
            blinked.append(int(str(stone)[mid:]))
        else:
            blinked.append(stone * 2024)
    return blinked


def blinks(wall: list[int], iterations: int) -> list[int]:
    for _ in range(iterations):
        wall = blink(wall)
    return wall


def solve(nums: list[int], iterations: int) -> int:
    counts: defaultdict[int, int] = defaultdict(int)

    # Initialize counts with input numbers
    for num in nums:
        counts[num] += 1

    for _ in range(iterations):
        next_counts: defaultdict[int, int] = defaultdict(int)

        for num, count in counts.items():
            if num == 0:
                next_counts[1] += count
            else:
                split_result = split_digits(num)
                if split_result:
                    a, b = split_result
                    next_counts[a] += count
                    next_counts[b] += count
                else:
                    next_counts[num * 2024] += count

        counts = next_counts

    return sum(counts.values())


def split_digits(num: int) -> tuple[int, int] | None:
    digits = len(str(num))
    if digits % 2 != 0:
        return None
    half = digits // 2
    divisor = 10**half
    return num // divisor, num % divisor


if __name__ == "__main__":
    assert blink(example_input) == example_output

    # PART A
    print(solve(real_input, 25))
    # PART B
    print(solve(real_input, 75))
