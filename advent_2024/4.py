from pathlib import Path

import numpy as np

test_grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


def count_word_in_grid(grid: list[str], word: str = "XMAS") -> int:
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    word_len = len(word)
    count = 0

    # Directions: (row_change, col_change)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                # Check all directions
                for dr, dc in directions:
                    rr, cc = r, c
                    match = True
                    for i in range(word_len):
                        if (
                            0 <= rr < rows
                            and 0 <= cc < cols
                            and grid[rr][cc] == word[i]
                        ):
                            rr += dr
                            cc += dc
                        else:
                            match = False
                            break
                    if match:
                        count += 1
    return count


def count_xmas_pattern(grid):
    # using numpy on here for speed and also because it's simpler
    grid = np.array([list(row) for row in grid])
    rows, cols = grid.shape
    if rows < 3 or cols < 3:
        return 0
    is_m = (grid == "M").astype(np.int8)
    is_a = (grid == "A").astype(np.int8)
    is_s = (grid == "S").astype(np.int8)
    count = 0
    count += np.sum(
        is_m[:-2, :-2] * is_a[1:-1, 1:-1] * is_s[2:, 2:] * is_m[:-2, 2:] * is_s[2:, :-2]
    )
    count += np.sum(
        is_s[:-2, :-2] * is_a[1:-1, 1:-1] * is_m[2:, 2:] * is_s[:-2, 2:] * is_m[2:, :-2]
    )
    count += np.sum(
        is_m[:-2, :-2] * is_a[1:-1, 1:-1] * is_s[2:, 2:] * is_s[:-2, 2:] * is_m[2:, :-2]
    )
    count += np.sum(
        is_s[:-2, :-2] * is_a[1:-1, 1:-1] * is_m[2:, 2:] * is_m[:-2, 2:] * is_s[2:, :-2]
    )
    return count


word = "XMAS"
assert count_word_in_grid(test_grid, word) == 18

text: list[str] = Path("advent_2024/4_input.txt").read_text().splitlines()
print(count_word_in_grid(text, word))

assert count_xmas_pattern(test_grid) == 9
print(count_xmas_pattern(text))
