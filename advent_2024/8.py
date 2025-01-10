import itertools
import math
from pathlib import Path


def read_input(file_path: Path) -> list[list[str]]:
    return [list(line) for line in Path(file_path).read_text().splitlines()]


def create_mapping(data: list[list[str]]) -> dict[tuple[int, int], str]:
    return {(i, j): value for i, row in enumerate(data) for j, value in enumerate(row)}


def get_antenna_info(
    mapping: dict[tuple[int, int], str],
) -> dict[str, list[tuple[int, int]]]:
    antenna_info: dict[str, list[tuple[int, int]]] = {}
    for (i, j), value in mapping.items():
        if value != ".":
            antenna_info.setdefault(value, []).append((i, j))
    return antenna_info


def add_antinode(bounds: int, nodes: set[tuple[int, int]], x: int, y: int) -> None:
    if 0 <= x < bounds and 0 <= y < bounds:
        nodes.add((x, y))


def part1(
    antenna_info: dict[str, list[tuple[int, int]]], bounds: int
) -> set[tuple[int, int]]:
    antinodes: set[tuple[int, int]] = set()
    for positions in antenna_info.values():
        for pos1, pos2 in itertools.combinations(positions, 2):
            dX = pos2[0] - pos1[0]
            dY = pos2[1] - pos1[1]
            add_antinode(bounds, antinodes, pos1[0] - dX, pos1[1] - dY)
            add_antinode(bounds, antinodes, pos2[0] + dX, pos2[1] + dY)
    return antinodes


def add_line_points(
    bounds: int,
    locations: set[tuple[int, int]],
    start: tuple[int, int],
    dX: int,
    dY: int,
) -> None:
    while 0 <= start[0] < bounds and 0 <= start[1] < bounds:
        locations.add(start)
        start = (start[0] + dX, start[1] + dY)


def part2(
    antenna_info: dict[str, list[tuple[int, int]]], bounds: int
) -> set[tuple[int, int]]:
    locations: set[tuple[int, int]] = set()
    for positions in antenna_info.values():
        for pos1, pos2 in itertools.combinations(positions, 2):
            dX = pos2[0] - pos1[0]
            dY = pos2[1] - pos1[1]
            locations.update([pos1, pos2])

            if dX == 0:
                locations.update((i, pos1[1]) for i in range(bounds))
            elif dY == 0:
                locations.update((pos1[0], i) for i in range(bounds))
            else:
                gcd = math.gcd(dX, dY)
                dX //= gcd
                dY //= gcd
                add_line_points(
                    bounds, locations, (pos1[0] - dX, pos1[1] - dY), -dX, -dY
                )
                add_line_points(bounds, locations, (pos2[0] + dX, pos2[1] + dY), dX, dY)
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
