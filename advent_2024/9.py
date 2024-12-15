from pathlib import Path

example_map = "2333133121414131402"
example_blocks = "00...111...2...333.44.5555.6666.777.888899"
example_compacted = "0099811188827773336446555566.............."


def show_blocks(disk_map: str) -> list[int | str]:
    blocks: list[str | int] = []
    block_number = 0
    for i in range(0, len(disk_map), 2):
        blocks.extend([block_number] * int(disk_map[i]))
        if i + 1 < len(disk_map):
            blocks.extend(["."] * int(disk_map[i + 1]))
            block_number += 1
    return blocks


def compact1(blocks: list[int | str]) -> list[int | str]:
    left = 0
    right = len(blocks) - 1

    while left < right:
        if blocks[left] == "." and blocks[right] != ".":
            blocks[left], blocks[right] = blocks[right], blocks[left]
            left += 1
            right -= 1
        elif blocks[left] != ".":
            left += 1
        elif blocks[right] == ".":
            right -= 1
    return blocks


def compact2(blocks: list[int | str]) -> list[int | str]:
    file_lengths = {
        file_id: blocks.count(file_id) for file_id in set(blocks) if file_id != "."
    }
    max_file_id = max(
        (file_id for file_id in file_lengths if isinstance(file_id, int)), default=-1
    )

    for file_id in range(max_file_id, -1, -1):
        if file_id not in file_lengths:
            continue

        file_length = file_lengths[file_id]
        file_start = next((i for i, block in enumerate(blocks) if block == file_id), -1)
        if file_start == -1:
            continue

        best_free_start = next(
            (
                i
                for i in range(file_start)
                if blocks[i : i + file_length] == ["."] * file_length
            ),
            -1,
        )

        if best_free_start != -1:
            blocks[best_free_start : best_free_start + file_length] = [
                file_id
            ] * file_length
            blocks = [
                "." if block == file_id and i >= file_start else block
                for i, block in enumerate(blocks)
            ]

    return blocks


def checksum(compact_blocks: list[int | str]) -> int:
    return sum(
        pos * int(char) for pos, char in enumerate(compact_blocks) if char != "."
    )


if __name__ == "__main__":
    real_input = Path("advent_2024/9_input.txt").read_text().strip()
    print(checksum(compact1(show_blocks(real_input))))
    print(checksum(compact2(show_blocks(real_input))))
