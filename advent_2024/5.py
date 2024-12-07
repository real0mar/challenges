from collections import defaultdict, deque
from pathlib import Path

lines: list[str] = (
    Path("advent_2024/5_input.txt").read_text(encoding="utf-8").splitlines()
)

rules: list[tuple[int, int]] = []
updates: list[list[int]] = []

for line in lines:
    curr_line = line.strip()
    if "|" in line:
        x, y = map(int, line.split("|"))
        rules.append((x, y))
    elif line and "," in line:
        updates.append(list(map(int, line.split(","))))


def build_graph(
    rules: list[tuple[int, int]]
) -> tuple[dict[int, list[int]], dict[int, int]]:
    graph: dict[int, list[int]] = defaultdict(list)
    in_degree: dict[int, int] = defaultdict(int)
    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0
    return graph, in_degree


def is_correct_order(update: list[int]) -> bool:
    position: dict[int, int] = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in position and y in position and position[x] > position[y]:
            return False
    return True


def topological_sort(update: list[int]) -> list[int]:
    relevant_pages = set(update)
    sub_graph: dict[int, list[int]] = defaultdict(list)
    sub_in_degree: dict[int, int] = defaultdict(int)
    for node in relevant_pages:
        sub_in_degree[node] = 0
    for x, y in rules:
        if x in relevant_pages and y in relevant_pages:
            sub_graph[x].append(y)
            sub_in_degree[y] += 1

    queue: deque[int] = deque([node for node in update if sub_in_degree[node] == 0])
    sorted_update: list[int] = []
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in sub_graph[node]:
            sub_in_degree[neighbor] -= 1
            if sub_in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_update


def middle_page_sum(updates: list[list[int]]) -> int:
    total: int = 0
    for update in updates:
        mid_index = len(update) // 2
        total += update[mid_index]
    return total


correct_updates: list[list[int]] = []
incorrect_updates: list[list[int]] = []
graph, in_degree = build_graph(rules)

for update in updates:
    if is_correct_order(update):
        correct_updates.append(update)
    else:
        incorrect_updates.append(update)

part1_result: int = middle_page_sum(correct_updates)

fixed_updates: list[list[int]] = []
for update in incorrect_updates:
    sorted_update = topological_sort(update)
    fixed_updates.append(sorted_update)

part2_result: int = middle_page_sum(fixed_updates)

print("Part 1:", part1_result)
print("Part 2:", part2_result)
