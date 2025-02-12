from collections import deque

test_grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

test_grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]


def numIslands(grid: list[list[str]]) -> int:

    def search(row: int, col: int) -> None:
        queue = deque([(row, col)])
        # Use collections.deque() for performance when using a queue NOT as a stack (popping from left)
        while queue:
            r, c = queue.popleft()
            # if I change this to pop() it becomes depth first search
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                grid[r][c] = "0"
                # don't have to track visits this time, can just map all visits to 0
                queue.extend([(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)])

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                islands += 1
                search(row, col)

    return islands


assert numIslands(test_grid1) == 1
assert numIslands(test_grid2) == 3
