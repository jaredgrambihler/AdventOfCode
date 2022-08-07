import bisect
import copy
from dataclasses import dataclass

with open("2021/input/day15input.txt") as f:
    input_text = f.read().strip()

MAX_VAL = 9999999

grid = [[int(c) for c in line] for line in input_text.splitlines()]


@dataclass
class ExplorePoint:
    row: int
    col: int
    path: list[tuple[int, int]]
    total_cost: int


def explore_point(grid: list[list[int]], cost: list[list[int]], explore_point: ExplorePoint) -> list[ExplorePoint]:
    row = explore_point.row
    col = explore_point.col
    total_cost = explore_point.total_cost + grid[row][col]
    if total_cost >= cost[row][col]:
        return []
    else:
        cost[row][col] = total_cost
    new_points = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    # Filter rows
    new_points = list(filter(lambda x : x[0] >= 0 and x[0] < len(grid), new_points))
    # Filter col
    new_points = list(filter(lambda x : x[1] >= 0 and x[1] < len(grid[0]), new_points))
    # Avoid existing points
    new_points = list(filter(lambda x : (x[0], x[1]) not in explore_point.path, new_points))
    new_path = copy.copy(explore_point.path)
    new_path.append((row, col))
    return [ExplorePoint(x[0], x[1], new_path, total_cost) for x in new_points]


def solve(grid: list[list[int]]):
    cost = [[MAX_VAL for _ in range(len(grid[0]))] for _ in range(len(grid))]
    to_explore = [ExplorePoint(0, 1, [(0,0)], 0), ExplorePoint(1, 0, [(0, 0)], 0)]
    while to_explore:
        point = to_explore.pop(0)
        if point.row == len(grid) - 1 and point.col == len(grid[0]) - 1:
            return point.total_cost + grid[point.row][point.col]
        new_to_explore = explore_point(grid, cost, point)
        for new_point in new_to_explore:
            bisect.insort(to_explore, new_point, key = lambda x : x.total_cost)


def increment_grid(grid: list[list[int]]) -> list[list[int]]:
    grid = copy.deepcopy(grid)
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            grid[i][j] += 1
            if grid[i][j] == 10:
                grid[i][j] = 1
    return grid


def create_large_grid(grid: list[list[int]], repeat_factor: int = 5) -> list[list[int]]:
    rows = len(grid)
    cols = len(grid[0])
    # Repeat right
    left_to_right_grids: list[list[list[int]]] = [grid]
    for _ in range(repeat_factor - 1):
        left_to_right_grids.append(increment_grid(left_to_right_grids[-1]))
    # Combine grids
    top_grid = left_to_right_grids.pop(0)
    while left_to_right_grids:
        cur_grid = left_to_right_grids.pop(0)
        for i, (row, cur_row) in enumerate(zip(top_grid, cur_grid)):
            top_grid[i] = row + cur_row
    # Repeat down
    top_to_bottom_grids: list[list[list[int]]] = [top_grid]
    for _ in range(repeat_factor - 1):
        top_to_bottom_grids.append(increment_grid(top_to_bottom_grids[-1]))
    total_grid = []
    for row_grid in top_to_bottom_grids:
        total_grid.extend(row_grid)
    return total_grid


if __name__ == "__main__":
    print(f"Part 1: {solve(grid)}")
    print(f"Part 2: {solve(create_large_grid(grid))}")
