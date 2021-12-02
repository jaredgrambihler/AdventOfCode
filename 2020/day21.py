import copy
import os
import re
import sys
from collections import Counter
import numpy as np
from pprint import pprint

try:
    day = re.findall("\d+", os.path.basename(__file__))[0]
except IndexError:
    print("No day in file")
    sys.exit()


def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    allergen_to_possible = dict()

    all_ingredients = []

    for line in text.splitlines():
        parts = line.split("(contains")
        ingredients = [x.strip() for x in parts[0].strip().split()]
        all_ingredients += ingredients
        allergens = [x.strip() for x in parts[1].replace(")", "").strip().split(",")]
        for allergen in allergens:
            # print("Allergen:", allergen)
            # print("Ingredients:", ingredients)
            cur_set = set(ingredients)
            if allergen in allergen_to_possible:
                combined = allergen_to_possible[allergen].intersection(cur_set)
                # print(combined)
                allergen_to_possible[allergen] = combined
            else:
                allergen_to_possible[allergen] = cur_set
    # print(allergen_to_possible)
    count = 0
    for ingredient in all_ingredients:
        found = False
        for s in allergen_to_possible.values():
            if ingredient in s:
                found = True
                break
        if not found:
            count += 1
    return count
    

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    allergen_to_possible = dict()

    for line in text.splitlines():
        parts = line.split("(contains")
        ingredients = [x.strip() for x in parts[0].strip().split()]
        allergens = [x.strip() for x in parts[1].replace(")", "").strip().split(",")]
        for allergen in allergens:
            cur_set = set(ingredients)
            if allergen in allergen_to_possible:
                combined = allergen_to_possible[allergen].intersection(cur_set)
                allergen_to_possible[allergen] = combined
            else:
                allergen_to_possible[allergen] = cur_set

    while not all(len(s) == 1 for s in allergen_to_possible.values()):
        found = set()
        for ingredient, possible in allergen_to_possible.items():
            if len(possible) == 1:
                found = found.union(possible)
        
        for ingredient, possible in allergen_to_possible.items():
            if len(possible) == 1:
                continue
            else:
                to_remove = []
                for x in possible:
                    if x in found:
                        to_remove.append(x)
                for x in to_remove:
                    possible.remove(x)
    allergen_to_possible = [(ingredient, list(s)[0]) for ingredient, s in allergen_to_possible.items()]
    allergen_to_possible = sorted(allergen_to_possible, key = lambda x: x[0])
    return ",".join(x[1] for x in allergen_to_possible)
    
print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test.txt"))
print(solve2(f"input/day{day}input.txt"))
