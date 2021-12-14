from collections import Counter

with open("input/day14input.txt") as f:
    input_text = f.read()


lines = input_text.splitlines()
polymer_str = lines[0]
START_CHAR = polymer_str[0]
END_CHAR = polymer_str[-1]
# store polymer as a dict of pairs to their count
polymer = Counter()
for i in range(len(polymer_str) - 1):
    polymer[polymer_str[i:i+2]] += 1


group_to_insert = dict()
for line in lines[1:]:
    if line.strip() == "":
        continue
    group, insert = line.strip().split(" -> ")
    group_to_insert[group] = insert


def step(polymer, group_to_insert):
    new_polymer = Counter()
    for pair, count in polymer.items():
        if pair in group_to_insert:
            # add in two new pairs with the given count
            middle_char = group_to_insert[pair]
            new_polymer[pair[0] + middle_char] += count
            new_polymer[middle_char + pair[1]] += count
        else:
            new_polymer[pair] = count
    return new_polymer


def apply_steps(polymer, group_to_insert, num_steps):
    for _ in range(num_steps):
        polymer = step(polymer, group_to_insert)
    return polymer


def min_max_diff(polymer, group_to_insert, steps):
    polymer = apply_steps(polymer, group_to_insert, steps)
    letter_to_count = Counter()
    for pair, count in polymer.items():
        for c in pair:
            letter_to_count[c] += count
    # every letter appears twice, unless it is the start or end, in which
    # case it won't appear twice for one of it's occurences
    for letter, count in letter_to_count.items():
        if letter == START_CHAR or letter == END_CHAR:
            letter_to_count[letter] = (count + 1) / 2
        else:
            letter_to_count[letter] = count / 2
    min_count = min(letter_to_count.values())
    max_count = max(letter_to_count.values())
    return int(max_count - min_count)


print("Part 1")
print(f"Difference between max and min count:  {min_max_diff(polymer, group_to_insert, 10)}")
print("Part 2")
print(f"Difference between max and min count:  {min_max_diff(polymer, group_to_insert, 40)}")
