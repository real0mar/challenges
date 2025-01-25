def numIslands(grid: list[list[str]]) -> int:
    checked_grid: list[list[bool]] = [
        [False for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]
    islands = 0
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "0":
                checked_grid[y][x] = True
            elif not checked_grid[y][x]:
                checked_grid = check_island(grid, checked_grid, y, x)
            else:
                continue

    return 0


def check_island(
    grid: list[list[str]], checked_grid: list[list[bool]], y: int, x: int
) -> list[list[bool]]:
    pass


grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

assert numIslands(grid1) == 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

assert numIslands(grid2) == 3
