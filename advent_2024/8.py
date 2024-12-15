import itertools
import math
from pathlib import Path

def read_input(file_path: Path) -> list[list[str]]:
    data = Path(file_path).read_text()
    return [list(line) for line in data.splitlines()]

def create_mapping(data: list[list[str]]) -> dict[tuple[int, int], str]:
    mapping: dict[tuple[int, int], str] = {}
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            mapping[i, j] = value
    return mapping

def get_antenna_info(mapping: dict[tuple[int, int], str]) -> dict[str, list[tuple[int, int]]]:
    antenna_info: dict[str, list[tuple[int, int]]] = {}
    for (i, j), value in mapping.items():
        if value != ".":
            antenna_info.setdefault(value, []).append((i, j))
    return antenna_info

def part1(antenna_info: dict[str, list[tuple[int, int]]], bounds: int) -> set[tuple[int, int]]:
    antinodes: set[tuple[int, int]] = set()
    for key in antenna_info:
        for pair in itertools.product(antenna_info[key], repeat=2):
            if pair[0] != pair[1]:
                dX = pair[1][0] - pair[0][0]
                dY = pair[1][1] - pair[0][1]
                antinode0 = (pair[0][0] - dX, pair[0][1] - dY)
                if 0 <= antinode0[0] < bounds and 0 <= antinode0[1] < bounds:
                    antinodes.add(antinode0)
                antinode1 = (pair[1][0] + dX, pair[1][1] + dY)
                if 0 <= antinode1[0] < bounds and 0 <= antinode1[1] < bounds:
                    antinodes.add(antinode1)
    return antinodes

def part2(antenna_info: dict[str, list[tuple[int, int]]], bounds: int) -> set[tuple[int, int]]:
    locations: set[tuple[int, int]] = set()
    for key in antenna_info:
        for pair in itertools.product(antenna_info[key], repeat=2):
            if pair[0] != pair[1]:
                dX = pair[1][0] - pair[0][0]
                dY = pair[1][1] - pair[0][1]
                locations.add(pair[0])
                locations.add(pair[1])
                if dX == 0:
                    for i in range(bounds):
                        locations.add((i, pair[0][1]))
                if dY == 0:
                    for i in range(bounds):
                        locations.add((pair[0][0], i))
                if math.gcd(dX, dY) != 0:
                    gcd = math.gcd(dX, dY)
                    dX //= gcd
                    dY //= gcd
                antinode0 = (pair[0][0] - dX, pair[0][1] - dY)
                while 0 <= antinode0[0] < bounds and 0 <= antinode0[1] < bounds:
                    locations.add(antinode0)
                    antinode0 = (antinode0[0] - dX, antinode0[1] - dY)
                antinode1 = (pair[1][0] + dX, pair[1][1] + dY)
                while 0 <= antinode1[0] < bounds and 0 <= antinode1[1] < bounds:
                    locations.add(antinode1)
                    antinode1 = (antinode1[0] + dX, antinode1[1] + dY)
    return locations

def main() -> None:
    file_path = Path("advent_2024/8_input.txt")
    data: list[list[str]] = read_input(file_path)
    mapping = create_mapping(data)
    bounds = len(data)

    antenna_info: dict[str, list[tuple[int, int]]] = get_antenna_info(mapping)

    part1_locations = part1(antenna_info, bounds)
    print(f"Part 1 answer: {len(part1_locations)}")

    part2_locations = part2(antenna_info, bounds)
    print(f"Part 2 answer: {len(part2_locations)}")

if __name__ == "__main__":
    main()
