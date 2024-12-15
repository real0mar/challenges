from pathlib import Path

example_map = "2333133121414131402"
example_blocks = "00...111...2...333.44.5555.6666.777.888899"
example_compacted = "0099811188827773336446555566.............."


def show_blocks(map: str) -> list[int | str]:
    is_block = True
    block_number: int = 0
    blocks: list[str | int] = []
    while map:
        if is_block:
            blocks.extend([block_number] * int(map[0]))
            map = map[1:]
            is_block = False
        else:
            blocks.extend(["."] * int(map[0]))
            is_block = True
            block_number += 1
            map = map[1:]
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
    file_lengths: dict[int | str, int] = {}
    for i, file_id in enumerate(blocks):
        if file_id != ".":
            if file_id not in file_lengths:
                file_lengths[file_id] = 0
            file_lengths[file_id] += 1

    max_file_id = 0
    for file_id in file_lengths:
        if isinstance(file_id, int) and file_id > max_file_id:
            max_file_id = file_id

    for file_id in range(max_file_id, -1, -1):
        if file_id not in file_lengths:
            continue

        file_length = file_lengths[file_id]
        file_start = -1
        for i in range(len(blocks)):
            if blocks[i] == file_id:
                file_start = i
                break
        if file_start == -1:
            continue

        best_free_start = -1
        for i in range(file_start):
            if blocks[i] == ".":
                free_space = 0
                for j in range(i, len(blocks)):
                    if blocks[j] == ".":
                        free_space += 1
                    else:
                        break
                if free_space >= file_length:
                    best_free_start = i
                    break

        if best_free_start != -1:
            for i in range(file_length):
                blocks[best_free_start + i] = file_id
            for i in range(file_start, len(blocks)):
                if blocks[i] == file_id:
                    blocks[i] = "."

    return blocks


def checksum(compact_blocks: list[int | str]) -> int:
    checksum = 0
    for pos, char in enumerate(compact_blocks):
        if char == ".":
            continue
        checksum += pos * int(char)
    return checksum


if __name__ == "__main__":
    real_input = Path("advent_2024/9_input.txt").read_text().strip()
    print(checksum(compact1(show_blocks(real_input))))
    print(checksum(compact2(show_blocks(real_input))))
