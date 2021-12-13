from dataclasses import dataclass

with open("input/day13input.txt") as f:
    input_text = f.read()


@dataclass
class Fold:
    axis: str
    line: int

point_lines, fold_lines = input_text.strip().split('\n\n')

points = []
folds = []

for line in point_lines.splitlines():
    x, y  = line.split(",")
    points.append((int(x), int(y)))

for fold in fold_lines.splitlines():
    axis, line = fold.split(" ")[-1].split("=")
    folds.append(Fold(axis, int(line)))


def fold(points, fold):
    if fold.axis == "x":
        point_index = 0
    else:
        point_index = 1
    folded_points = set()
    for point in points:
        new_point = [point[0], point[1]]
        if point[point_index] > fold.line:
            # get folded point value
            new_val = fold.line - (point[point_index] - fold.line)
            new_point[point_index] = new_val
        folded_points.add((new_point[0], new_point[1]))
    return list(folded_points)


def run_folds(points, folds):
    for x in folds:
        points = fold(points, x)
    return points


def print_points(points):
    points = set(points)
    max_x = max(point[0] for point in points)
    max_y = max(point[1] for point in points)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in points:
                print("#", end="")
            else:
                print(".", end="")
        print("\n", end="")


print("Part 1")
print(f"Number of points after first fold: {len(fold(points, folds[0]))}")
print("Part 2")
print(f"Printed points:\n{print_points(run_folds(points, folds))}")
