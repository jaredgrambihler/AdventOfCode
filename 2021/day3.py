with open("input/day3input.txt") as f:
    input_text = f.read()

lines = input_text.strip().splitlines()
bit_lines = [[int(c) for c in line] for line in lines]


def flip_bits(bits):
    return [0 if bit == 1 else 1 for bit in bits]


def compute_value(bits):
    amount = 0
    place_val = 1
    for bit in reversed(bits):
        if bit == 1:
            amount += place_val
        place_val *= 2
    return amount

def get_column_count(grid, count_value, col):
    count = 0
    for row in grid:
        if row[col] == count_value:
            count +=1
    return count


def get_column_counts(grid, count_value):
    return [get_column_count(grid, count_value, i) for i in range(len(grid[0]))]


def get_power(grid):
    total_rows = len(grid)
    gamma = [1 if one_count > total_rows - one_count else 0 for one_count in get_column_counts(grid, 1)]
    epsilon = flip_bits(gamma)
    return compute_value(gamma) * compute_value(epsilon)


def get_rating(grid, keep_bit_function):
    cur_lines = [line for line in grid]
    for i in range(len(grid[0])):
        one_count = get_column_count(cur_lines, 1, i)
        zero_count = len(cur_lines) - one_count
        keep = keep_bit_function(zero_count, one_count)
        cur_lines = [line for line in cur_lines if line[i] == keep]
        if len(cur_lines) == 1:
            break
    return compute_value(cur_lines[0])


def get_oxygen_rating(grid):
    def get_keep_bit_oxygen(zero_count, one_count):
        if zero_count > one_count:
            return 0
        else:
            return 1
    return get_rating(grid, get_keep_bit_oxygen)


def get_co2_rating(grid):
    def get_keep_bit_co2(zero_count, one_count):
        if zero_count <= one_count:
            return 0
        else:
            return 1
    return get_rating(grid, get_keep_bit_co2)


def get_life_support_rating(grid):
    return get_oxygen_rating(grid) * get_co2_rating(grid)


print("Part 1")
print(f"Power: {get_power(bit_lines)}")
print("Part 2")
print(f"Life support rating: {get_life_support_rating(bit_lines)}")