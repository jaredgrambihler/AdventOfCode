with open("input/day2input.txt") as f:
    input_text = f.read()

input_lines = input_text.strip().splitlines()

def get_position_value(lines):
    horiz = 0
    depth = 0
    for line in lines:
        direction, amount = line.split()
        amount = int(amount)
        if direction == "forward":
            horiz += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount
    return horiz * depth

def get_position_values_2(lines):
    horiz = 0
    depth = 0
    aim = 0
    for line in lines:
        direction, amount = line.split()
        amount = int(amount)
        if direction == "forward":
            horiz += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    return horiz * depth

print("Part 1")
print(f"Combined value: {get_position_value(input_lines)}")
print("Part 2")
print(f"Combined value: {get_position_values_2(input_lines)}")