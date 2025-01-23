real_input = [
    int(x) for x in ["6571", "0", "5851763", "526746", "23", "69822", "9", "989"]
]
example_input = [int(x) for x in ["0", "1", "10", "99", "999"]]
example_output = [int(x) for x in ["1", "2024", "1", "0", "9", "9", "2021976"]]


def blink(wall: list[int]) -> list[int]:
    blinked: list[int] = []
    for stone in wall:
        if stone == 0:
            blinked.append(1)
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            mid = len(str_stone) // 2
            blinked.append(int(str(stone)[:mid]))
            blinked.append(int(str(stone)[mid:]))
        else:
            blinked.append(stone * 2024)
    return blinked


def blinks(wall: list[int], iterations: int) -> list[int]:
    for _ in range(iterations):
        wall = blink(wall)
    return wall


def wall_length(wall: list[int], iterations: int) -> int:
    pass


if __name__ == "__main__":
    assert blink(example_input) == example_output

    # PART A
    print(len(blinks(real_input, 25)))
