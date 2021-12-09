with open("input/day9input.txt") as f:
    input_text = f.read()

# input_text = """
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# """

def get_grid(text):
    grid = []
    for line in text.splitlines():
        line = line.strip()
        if line == "":
            continue
        grid.append([int(c) for c in line])
    return grid


def pad_grid(grid):
    padded_grid = []
    max_val = 9
    padded_grid.append([max_val for _ in range(len(grid[0])+2)])
    for row in grid:
        padded_grid.append([max_val] + [x for x in row] + [max_val])
    padded_grid.append([max_val for _ in range(len(grid[0])+2)])
    return padded_grid


def get_low_points(grid):
    low_points = []
    grid = pad_grid(grid)
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            cur = grid[i][j]
            if cur < grid[i+1][j] and cur < grid[i][j+1] and cur < grid[i-1][j] and cur < grid[i][j-1]:
                low_points.append((i-1, j-1))
    return low_points


def get_risk_level_sum(grid):
    low_points = get_low_points(grid)
    risk_level_sum = 0
    for i, j in low_points:
        risk_level = grid[i][j] + 1
        risk_level_sum += risk_level
    return risk_level_sum


def get_basin_size(low_point, grid):
    size = 1
    search_points = [low_point]
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    while len(search_points) > 0:
        possible_next_search_points = []
        for search_point in search_points:
            i, j = search_point
            possible_next_search_points.extend([(i+1, j), (i, j+1), (i-1,j), (i, j-1)])
            visited[i][j] = True
        next_search_points = []
        for search_point in possible_next_search_points:
            i, j = search_point
            if i < 0 or j < 0:
                continue
            if i >= len(grid) or j >=len(grid[i]):
                continue
            if grid[i][j] == 9:
                continue
            if visited[i][j]:
                continue
            next_search_points.append(search_point)
        search_points = list(set(next_search_points))
        size += len(search_points)
    return size


def get_basin_sizes(grid):
    low_points = get_low_points(grid)
    basin_sizes = []
    for low_point in low_points:
        basin_sizes.append(get_basin_size(low_point, grid))
    return basin_sizes


def get_largest_three_basins_product(grid):
    basin_sizes = get_basin_sizes(grid)
    max_three = sorted(basin_sizes, reverse=True)[:3]
    product = 1
    for size in max_three:
        product *= size
    return product


grid = get_grid(input_text)

print("Part 1")
print(f"Risk level sum {get_risk_level_sum(grid)}")
print("Part 2")
print(f"Three largest basins product: {get_largest_three_basins_product(grid)}")
