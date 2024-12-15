from pathlib import Path

example_map = "2333133121414131402"
example_blocks = "00...111...2...333.44.5555.6666.777.888899"
example_compacted = "0099811188827773336446555566.............."


def show_blocks(map: str) -> str:
    is_block = True
    block_number = 0
    blocks = ""
    while map:
        if is_block:
            blocks += str(block_number) * int(map[0])
            map = map[1:]
            is_block = False
        else:
            blocks += "." * int(map[0])
            is_block = True
            block_number += 1
            map = map[1:]
    return blocks


assert show_blocks(example_map) == example_blocks


def compact(blocks: str) -> str:
    left = 0
    right = len(blocks) - 1

    while left < right:
        if blocks[left] == "." and blocks[right] != ".":
            blocks = (
                blocks[:left]
                + blocks[right]
                + blocks[left + 1 : right]
                + "."
                + blocks[right + 1 :]
            )
            left += 1
            right -= 1
        elif blocks[left] != ".":
            left += 1
        elif blocks[right] == ".":
            right -= 1
    return blocks

def checksum(compact_blocks: str) -> int:
    checksum = 0
    for pos, char in enumerate(compact_blocks):
        if char == ".":
            return checksum
        else:
            checksum += pos * int(char)


if __name__ == "__main__":
    real_input = Path("advent_2024/9_input.txt").read_text().strip()
    print(checksum(compact(show_blocks(real_input))))