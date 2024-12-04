import re
from pathlib import Path

MUL_REGEX = re.compile(r"mul\((-?\d+),(-?\d+)\)")
TRIM_REGEX = re.compile(r"(do\(\)|don't\(\))")


def trim(text: str) -> str:
    segments = TRIM_REGEX.split(text)
    include = True
    return "".join(
        segment if include else ""
        for segment in segments
        if (include := segment == "do()" or (include and segment != "don't()"))
    )


def process_text(file_path: str) -> int:
    text = Path(file_path).read_text()
    trimmed_text = trim(text)
    return sum(int(a) * int(b) for a, b in MUL_REGEX.findall(trimmed_text))


test_text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
trimmed_text = trim(test_text)
result = sum(int(a) * int(b) for a, b in MUL_REGEX.findall(trimmed_text))
print(result)

file_result = process_text("advent_2024/3_input.txt")
print(file_result)
