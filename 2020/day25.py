import copy
import os
import re
import sys
from collections import Counter
from pprint import pprint

try:
    day = re.findall("\d+", os.path.basename(__file__))[0]
except IndexError:
    print("No day in file")
    sys.exit()

def transform(subject_number, loop_size):
    val = 1
    for _ in range(loop_size):
        val *= subject_number
        val = val % 20201227
    return val

def find_loops(key):
    i = 0
    val = 1
    while True:
        if val == key:
            return i
        val *= 7
        val = val % 20201227
        i += 1

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    keys = [int(x) for x in text.splitlines()]
    card = keys[0]
    door = keys[1]
    print(door, card)
    # door_loops = find_loops(door)
    card_loops = find_loops(card)
    # print("door loops", door_loops, "\nCard loops", card_loops)
    return transform(door, card_loops)


def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    
    
print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test.txt"))
print(solve2(f"input/day{day}input.txt"))
