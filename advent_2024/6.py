from pathlib import Path

def parse_input(file_path):
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
    obstacle_set = set()
    start_x, start_y = None, None
    for y_coord, line in enumerate(lines):
        for x_coord, character in enumerate(line):
            if character == '#':
                obstacle_set.add((x_coord, y_coord))
            elif character == '^':
                start_x, start_y = x_coord, y_coord
    return obstacle_set, start_x, start_y, len(lines[0]), len(lines)

def part1(obstacle_set, start_x, start_y, x_bound, y_bound):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    visited_cells = set()
    direction_index = 0
    current_x, current_y = start_x, start_y

    while 0 <= current_x < x_bound and 0 <= current_y < y_bound:
        visited_cells.add((current_x, current_y))
        delta_x, delta_y = directions[direction_index]
        if (current_x + delta_x, current_y + delta_y) in obstacle_set:
            direction_index = (direction_index + 1) % 4
        else:
            current_x += delta_x
            current_y += delta_y

    return len(visited_cells), visited_cells

def part2(obstacle_set, start_x, start_y, visited_cells, x_bound, y_bound):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    obstruction_count = 0

    for potential_obstacle in visited_cells:
        temporary_obstacles = obstacle_set | {potential_obstacle}
        direction_index = 0
        temp_visited_states = set()
        current_x, current_y = start_x, start_y

        while 0 <= current_x < x_bound and 0 <= current_y < y_bound:
            delta_x, delta_y = directions[direction_index]
            if (current_x + delta_x, current_y + delta_y) in temporary_obstacles:
                if (current_x, current_y, delta_x, delta_y) in temp_visited_states:
                    obstruction_count += 1
                    break
                temp_visited_states.add((current_x, current_y, delta_x, delta_y))
                direction_index = (direction_index + 1) % 4
            else:
                current_x += delta_x
                current_y += delta_y

    return obstruction_count

def main():
    file_path = Path('advent_2024/6_input.txt')
    obstacle_set, start_x, start_y, x_bound, y_bound = parse_input(file_path)

    part1_result, visited_cells = part1(obstacle_set, start_x, start_y, x_bound, y_bound)
    print(f"Part 1: {part1_result}")

    part2_result = part2(obstacle_set, start_x, start_y, visited_cells, x_bound, y_bound)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()