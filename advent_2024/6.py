from pathlib import Path


def parse_input(file_path: Path) -> list[list[str]]:
    with Path.open(file_path, "r") as f:
        grid: list[list[str]] = [list(line.strip()) for line in f.readlines()]
    return grid


def simulate_patrol(grid: list[list[str]]) -> int:
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    turns = {"^": ">", ">": "v", "v": "<", "<": "^"}

    guard_pos: tuple[int, int] | None = None
    guard_dir: str | None = None

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                guard_pos = (r, c)
                guard_dir = cell
                grid[r][c] = "."
                break
        if guard_pos and guard_dir:
            break

    if not guard_pos:
        return 0

    visited = set()
    visited.add(guard_pos)
    rows, cols = len(grid), len(grid[0])

    while True:
        dr, dc = directions[guard_dir]
        nr, nc = guard_pos[0] + dr, guard_pos[1] + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            break

        if grid[nr][nc] == "#":
            guard_dir = turns[guard_dir]
        else:
            guard_pos = (nr, nc)
            visited.add(guard_pos)

    return len(visited)


grid = parse_input(Path("advent_2024/6_input.txt"))
distinct_positions: int = simulate_patrol(grid)
print(f"Distinct positions visited: {distinct_positions}")
