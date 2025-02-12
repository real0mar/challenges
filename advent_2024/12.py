from collections import deque
from pathlib import Path

Cell = tuple[int, int]
Grid = list[list[str]]
Region = tuple[str, list[Cell]]

map1 = """AAAA
BBCD
BBCC
EEEC"""

map2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

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

map4 = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

map5 = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
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


def part1(map_str: str, debug: bool = False) -> int:
    grid: Grid = parse_map(map_str)
    regions = find_regions(grid)
    total_cost = 0
    for plant_type, cells in regions:
        area = len(cells)
        perimeter = calculate_perimeter(grid, cells)
        cost = area * perimeter
        if debug:
            print(
                f"Region '{plant_type}': Area = {area}, Perimeter = {perimeter}, Cost = {cost}"
            )
        total_cost += cost
    if debug:
        print(f"Total fencing cost: {total_cost}")
    return total_cost


def count_sides(grid: Grid, region_cells: list[Cell]) -> int:
    """
    Improved approach: each continuous straight boundary segment is a 'side'.
    We'll:
      1) Gather all boundary edges for the region.
      2) Group adjacent collinear edges to count how many continuous runs exist.
    """
    region = set(region_cells)
    rows = len(grid)
    cols = len(grid[0])

    # We'll store edges in the form:
    #   horizontal edges => ('H', x, ystart, yend)
    #   vertical edges   => ('V', y, xstart, xend)
    #   where yend = ystart+1 for single cell boundaries, xend = xstart+1
    # Actually each cell boundary is length=1 in grid terms.
    # We'll group these single-segment edges if they're collinear and contiguous.
    horizontal_edges = []
    vertical_edges = []

    for (x, y) in region:
        # top edge
        if x == 0 or (x > 0 and (x-1, y) not in region):
            # horizontal from (x,y)->(x,y+1)
            horizontal_edges.append((x, y, y+1))
        # bottom edge
        if x == rows - 1 or (x < rows - 1 and (x+1, y) not in region):
            horizontal_edges.append((x+1, y, y+1))
        # left edge
        if y == 0 or (y > 0 and (x, y-1) not in region):
            vertical_edges.append((y, x, x+1))
        # right edge
        if y == cols - 1 or (y < cols - 1 and (x, y+1) not in region):
            vertical_edges.append((y+1, x, x+1))

    # Now we group horizontal edges by row.
    from collections import defaultdict
    horiz_by_row = defaultdict(list)
    for (row, y1, y2) in horizontal_edges:
        # always y2 == y1+1, but let's keep it general.
        if y2 < y1:
            y1, y2 = y2, y1
        horiz_by_row[row].append((y1, y2))

    # For each row, merge contiguous segments if they share endpoints AND are directly adjacent.
    # But each single edge is exactly from y1 to y1+1, so effectively each is length 1.
    # Consecutive edges in the same row with y1=1,y2=2 and next y1=2,y2=3 are a single run.

    def merge_1d_ranges(ranges: list[tuple[int,int]]) -> int:
        # each range is length=1, so we just count how many runs.
        # sort by start
        ranges.sort()
        runs = 0
        if not ranges:
            return 0
        current_start, current_end = ranges[0]
        runs = 1
        for (s, e) in ranges[1:]:
            if s == current_end:  # contiguous
                # extend current run
                current_end = e
            else:
                # start new run
                runs += 1
                current_start = s
                current_end = e
        return runs

    horiz_sides = 0
    for row, segs in horiz_by_row.items():
        horiz_sides += merge_1d_ranges(segs)

    vert_by_col = defaultdict(list)
    for (col, x1, x2) in vertical_edges:
        if x2 < x1:
            x1, x2 = x2, x1
        vert_by_col[col].append((x1,x2))

    vert_sides = 0
    for col, segs in vert_by_col.items():
        vert_sides += merge_1d_ranges(segs)

    return horiz_sides + vert_sides


def part2(map_str: str, debug: bool = False) -> int:
    grid = parse_map(map_str)
    regions = find_regions(grid)
    total_cost = 0
    for plant_type, cells in regions:
        area = len(cells)
        sides = count_sides(grid, cells)
        cost = area * sides
        if debug:
            print(f"Region '{plant_type}' => area={area}, sides={sides}, cost={cost}")
        total_cost += cost
    if debug:
        print(f"Total cost (part2) = {total_cost}")
    return total_cost


real_input = Path("advent_2024/12_input.txt").read_text()
print(part1(real_input))
print(part2(real_input))