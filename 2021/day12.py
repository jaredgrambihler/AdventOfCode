import copy

with open("input/day12input.txt") as f:
    input_text = f.read()


def get_cave_to_connected_caves(lines):
    cave_to_connected_caves = dict()
    for line in lines:
        start, end = line.split("-")
        start_set = cave_to_connected_caves.get(start, set())
        end_set = cave_to_connected_caves.get(end, set())
        start_set.add(end)
        end_set.add(start)
        cave_to_connected_caves[start] = start_set
        cave_to_connected_caves[end] = end_set
    return cave_to_connected_caves


def get_num_paths_helper(cave_to_connected_caves, current_cave, visited_caves):
    if current_cave == 'end':
        return 1
    visited_caves.add(current_cave)
    next_caves = cave_to_connected_caves[current_cave]
    num_paths = 0
    for cave in next_caves:
        if cave in visited_caves and cave.lower() == cave:
            continue
        else:
            num_paths += get_num_paths_helper(cave_to_connected_caves, cave, copy.copy(visited_caves))
    return num_paths


def get_num_paths(cave_to_connected_caves):
    return get_num_paths_helper(cave_to_connected_caves, 'start', set())


def get_num_paths_helper_2(cave_to_connected_caves, current_cave, visited_caves, visited_small_twice):
    if current_cave == 'end':
        return 1
    visited_caves.add(current_cave)
    next_caves = cave_to_connected_caves[current_cave]
    num_paths = 0
    for cave in next_caves:
        if cave in visited_caves and cave.lower() == cave:
            if not visited_small_twice and cave != 'start':
                num_paths += get_num_paths_helper_2(cave_to_connected_caves, cave, copy.copy(visited_caves), True)
        else:
            num_paths += get_num_paths_helper_2(cave_to_connected_caves, cave, copy.copy(visited_caves), visited_small_twice)
    return num_paths


def get_num_paths_2(cave_to_connected_caves):
    return get_num_paths_helper_2(cave_to_connected_caves, 'start', set(), False)


lines = input_text.strip().splitlines()
cave_to_connected_caves = get_cave_to_connected_caves(lines)

print(cave_to_connected_caves)
print("Part 1")
print(f"Number of paths: {get_num_paths(cave_to_connected_caves)}")
print("Part 2")
print(f"Number of paths: {get_num_paths_2(cave_to_connected_caves)}")

