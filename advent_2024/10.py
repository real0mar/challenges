from collections import deque
from pathlib import Path

test_input = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732",
]


def calculate_trailhead_scores(topographic_map: list[str]) -> int:
    rows, cols = len(topographic_map), len(topographic_map[0])
    grid = [[int(cell) for cell in row] for row in topographic_map]

    def bfs(start: tuple[int, int]) -> set[tuple[int, int]]:
        queue = deque([start])
        visited = set([start])
        reachable_nines: set[tuple[int, int]] = set()

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    if grid[nx][ny] == grid[x][y] + 1:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        if grid[nx][ny] == 9:
                            reachable_nines.add((nx, ny))
        return reachable_nines

    total_score = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                score = len(bfs((r, c)))
                total_score += score

    return total_score


def calculate_trailhead_ratings(topographic_map: list[str]) -> int:
    rows, cols = len(topographic_map), len(topographic_map[0])
    grid = [[int(cell) for cell in row] for row in topographic_map]

    def dfs(x: int, y: int) -> int:
        stack = [[(x, y)]]
        trails = 0

        while stack:
            path = stack.pop()
            cx, cy = path[-1]

            if grid[cx][cy] == 9:
                trails += 1
                continue

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in path:
                    if grid[nx][ny] == grid[cx][cy] + 1:
                        stack.append(path + [(nx, ny)])

        return trails

    total_rating = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                total_rating += dfs(r, c)

    return total_rating


if __name__ == "__main__":
    terrain_input = [
        line.strip()
        for line in Path("advent_2024/10_input.txt").read_text().splitlines()
    ]

    # PART A

    assert calculate_trailhead_scores(test_input) == 36
    print(calculate_trailhead_scores(terrain_input))

    # PART B

    assert calculate_trailhead_ratings(test_input) == 81
    print(calculate_trailhead_ratings(terrain_input))
