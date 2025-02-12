from collections import defaultdict

def main():
    with open("advent_2024/12_input.txt") as f:
        grid = [list(line.strip()) for line in f]

    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    total = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                current_type = grid[i][j]
                queue = [(i, j)]
                visited[i][j] = True
                region = []
                for r, c in queue:
                    region.append((r, c))
                    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == current_type:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                horizontal_edges = defaultdict(list)
                vertical_edges = defaultdict(list)
                for r, c in region:
                    if r == 0 or grid[r-1][c] != current_type:
                        horizontal_edges[r].append(c)
                    if r == rows-1 or grid[r+1][c] != current_type:
                        horizontal_edges[r+1].append(c)
                    if c == cols-1 or grid[r][c+1] != current_type:
                        vertical_edges[c+1].append(r)
                    if c == 0 or grid[r][c-1] != current_type:
                        vertical_edges[c].append(r)
                horizontal_segments = 0
                for y in horizontal_edges:
                    x_list = sorted(horizontal_edges[y])
                    if not x_list:
                        continue
                    current = x_list[0]
                    segments = 1
                    for x in x_list[1:]:
                        if x != current + 1:
                            segments += 1
                        current = x
                    horizontal_segments += segments
                vertical_segments = 0
                for x in vertical_edges:
                    y_list = sorted(vertical_edges[x])
                    if not y_list:
                        continue
                    current = y_list[0]
                    segments = 1
                    for y in y_list[1:]:
                        if y != current + 1:
                            segments += 1
                        current = y
                    vertical_segments += segments
                total_sides = horizontal_segments + vertical_segments
                area = len(region)
                total += area * total_sides
    print(total)

if __name__ == '__main__':
    main()