from collections import deque

Cell = tuple[int, int]
Grid = list[list[str]]
Region = tuple[str, list[Cell]]


def parse_map(map_str: str) -> Grid:
    return [list(line) for line in map_str.strip().split("\n")]


def get_neighbors(x: int, y: int, rows: int, cols: int) -> list[Cell]:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors: list[Cell] = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))
    return neighbors


def find_regions(grid: Grid) -> list[Region]:
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    regions: list[Region] = []

    for x in range(rows):
        for y in range(cols):
            if not visited[x][y]:
                visited[x][y] = True
                plant_type = grid[x][y]
                queue: deque[Cell] = deque()
                queue.append((x, y))
                region_cells: list[Cell] = []

                while queue:
                    cx, cy = queue.popleft()
                    region_cells.append((cx, cy))
                    for nx, ny in get_neighbors(cx, cy, rows, cols):
                        if not visited[nx][ny] and grid[nx][ny] == plant_type:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

                regions.append((plant_type, region_cells))
    return regions


def calculate_perimeter(grid: Grid, region_cells: list[Cell]) -> int:
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for x, y in region_cells:
        sides = 4
        for nx, ny in get_neighbors(x, y, rows, cols):
            if grid[nx][ny] == grid[x][y]:
                sides -= 1
        perimeter += sides
    return perimeter


def calculate_total_fencing_cost(map_str: str) -> int:
    grid: Grid = parse_map(map_str)
    regions = find_regions(grid)
    total_cost = 0
    for plant_type, cells in regions:
        area = len(cells)
        perimeter = calculate_perimeter(grid, cells)
        cost = area * perimeter
        print(
            f"Region '{plant_type}': Area = {area}, Perimeter = {perimeter}, Cost = {cost}"
        )
        total_cost += cost
    print(f"Total fencing cost: {total_cost}")
    return total_cost


# First Example
map1 = """AAAA
BBCD
BBCC
EEEC"""

print("First Example:")
calculate_total_fencing_cost(map1)
print("\n")

# Second Example
map2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

print("Second Example:")
calculate_total_fencing_cost(map2)
print("\n")

# Larger Example
map3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

print("Larger Example:")
calculate_total_fencing_cost(map3)
