from collections import Counter

with open("input/day14input.txt") as f:
    input_text = f.read()

lines = input_text.splitlines()
polymer = lines[0]

group_to_insert = dict()
for line in lines[1:]:
    if line.strip() == "":
        continue
    group, insert = line.strip().split(" -> ")
    group_to_insert[group] = insert


def step(polymer, group_to_insert):
    new_str = []
    for i, c in enumerate(polymer):
        double_char = polymer[i:i+2] # at the end this will only be a single char but won't break
        new_str.append(c)
        if double_char in group_to_insert:
            new_str.append(group_to_insert[double_char])
    return "".join(new_str)


def apply_steps(polymer, group_to_insert, num_steps):
    for _ in range(num_steps):
        polymer = step(polymer, group_to_insert)
    return polymer


def min_max_diff(polymer, group_to_insert, steps):
    polymer = apply_steps(polymer, group_to_insert, steps)
    min_count = len(polymer)
    max_count = 0
    for _, count in Counter(polymer).items():
        if count > max_count:
            max_count = count
        if count < min_count:
            min_count = count
    return max_count - min_count


print("Part 1")
print(f"Difference between max and min count:  {min_max_diff(polymer, group_to_insert, 10)}")
print("Part 2")
print(f"Difference between max and min count:  {min_max_diff(polymer, group_to_insert, 40)}")
