from pathlib import Path
from time import time

EXAMPLE = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

REAL_IN = Path("advent_2024/8_input.txt").read_text()


def part1(input: list[list[str]]) -> int:
    antinodes = set()
    seen_frequencies = set()
    for y, row in enumerate(input):
        for x, cell in enumerate(row):
            if cell.isalnum() and cell not in seen_frequencies:
                seen_frequencies.add(cell)
            elif cell.isalnum():
                pass
            # there is probably a faster way. will think about it


def part2(input: str) -> int:
    return -1


if __name__ == "__main__":
    start = time()
    example_data = [list(line) for line in EXAMPLE.splitlines()]
    real_data = [list(line) for line in REAL_IN.splitlines()]
    assert part1(example_data) == 14
    assert part2(EXAMPLE) == 11387

    print(part1(REAL_IN))
    print(part2(REAL_IN))
    print(f"Time: {time() - start}")
