from collections import Counter

left: list[int] = []
right: list[int] = []


with open("advent_2024/1_input.txt") as f:
    for line in f:
        numbers = line.strip().split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

left.sort()
right.sort()

distance: int = sum(abs(a - b) for a, b in zip(left, right))
print(distance)

right_counter: Counter = Counter(right)

similarity: int = 0
for number in left:
    similarity += right_counter.get(number, 0) * number

print(similarity)
