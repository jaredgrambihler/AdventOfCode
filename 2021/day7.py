with open("input/day7input.txt") as f:
    input_text = f.read()

horizontal_positions = [int(x) for x in input_text.strip().split(",")]

def part1_cost_function(x1, x2):
    return abs(x1 - x2)

def part2_cost_function(x1, x2):
    distance = abs(x1 - x2)
    # sum is 1 + 2 + 3 + ... + distance
    # this is sum of first n numbers
    return distance * (distance + 1) / 2

def get_fuel_cost(horiz_pos, positions, cost_function):
    fuel = 0
    for position in positions:
        fuel += cost_function(position, horiz_pos)
    return fuel

def get_min_cost(positions, cost_function):
    min_cost = 9999999999999
    for i in range(min(horizontal_positions), max(horizontal_positions)):
        min_cost = min(get_fuel_cost(i, horizontal_positions, cost_function), min_cost)
    return min_cost



print("Part 1")
print(f"Min cost {get_min_cost(horizontal_positions, part1_cost_function)}")

print("Part 2")
print(f"Min cost {get_min_cost(horizontal_positions, part2_cost_function)}")
