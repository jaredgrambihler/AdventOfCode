from collections import Counter

with open('input/day5input.txt') as f:
    input_text = f.read()

input_lines = input_text.strip().splitlines()

def get_lines(input_lines):
    lines = []
    for line in input_lines:
        line = line.strip()
        coord1, coord2 = line.split(" -> ")
        x1, y1 = coord1.split(',')
        x2, y2 = coord2.split(',')
        lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return lines


def get_vertical_or_horizontal_lines(lines):
    filtered_lines = []
    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            filtered_lines.append(line)
    return filtered_lines


def get_num_overlapping_lines(lines):
    index_to_count = Counter()
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]
        if x1 == x2:
            max_y = max(y1, y2)
            min_y = min(y1, y2)
            for y in range(min_y, max_y + 1):
                index_to_count[(x1, y)] += 1
        elif y1 == y2:
            max_x = max(x1, x2)
            min_x = min(x1, x2)
            for x in range(min_x, max_x + 1):
                index_to_count[(x, y1)] += 1
        else:
            # diagonal
            x_distance = abs(x2 - x1)
            y_distance = abs(y2 - y1)
            x_direction = (x2 - x1) / x_distance
            y_direciton = (y2 - y1) / y_distance
            assert x_distance == y_distance
            for i in range(x_distance + 1):
                x_offset = x_direction * i
                y_offset = y_direciton * i
                index_to_count[(x1 + x_offset, y1 + y_offset)] += 1
    overlapping = 0
    for val in index_to_count.values():
        if val > 1:
            overlapping += 1
    return overlapping


lines = get_lines(input_lines)

print("Part 1")
print(f"Number of overlapping lines: {get_num_overlapping_lines(get_vertical_or_horizontal_lines(lines))}")
print("Part 2")
print(f"Number of overlapping lines: {get_num_overlapping_lines(lines)}")
