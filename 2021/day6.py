from collections import Counter

with open("input/day6input.txt") as f:
    input_text = f.read()

fish_ages = [int(x) for x in input_text.strip().split(",")]

age_to_count = Counter(fish_ages)

def get_num_fish(age_to_count, days):
    for day in range(days):
        next_age_to_count = Counter()
        for age, count in age_to_count.items():
            if age == 0:
                next_age_to_count[8] += count
                next_age_to_count[6] += count
            else:
                next_age_to_count[age - 1] += count
        age_to_count = next_age_to_count
    return sum(age_to_count.values())

print(age_to_count)

print("Part 1")
print(f"Total fish after 80 days: {get_num_fish(age_to_count, 80)}")

print("Part 2")
print(f"Total fish after 256 days: {get_num_fish(age_to_count, 256)}")
