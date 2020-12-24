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
    all_directions = []
    for line in text.splitlines():
        directions = []
        i = 0
        while i < len(line) - 1:
            if line[i] == 's' or line[i] == 'n':
                directions.append(line[i] + line[i+1])
                i += 2
            elif line[i] == 'e' or line[i] == 'w':
                directions.append(line[i])
                i += 1
            else:
                print("Not possible")
        directions.append(line[-1])
        all_directions.append(directions)
    # represent tiles as alternating rows, cols
    # so full grid is
    # 1 0 1 0
    # 0 1 0 1
    # where 0 means nothing
    # find the point of each tile from directions
    black_tiles = set()
    c = Counter()
    for directions in all_directions:
        x = 0
        y = 0
        for direction in directions:
            if direction == "e":
                x += 2
            elif direction == "w":
                x -= 2
            elif direction == "nw":
                x -= 1
                y += 1
            elif direction == "ne":
                x += 1
                y += 1
            elif direction == "sw":
                x -= 1
                y -= 1
            elif direction == "se":
                x += 1
                y -= 1
            else:
                print("not possible")
        tile = (x, y)
        c[tile] += 1
        if tile in black_tiles:
            # flip back to white if it is black
            black_tiles.remove(tile)
        else:
            # make it black
            black_tiles.add(tile)
    print(c)
    return len(black_tiles)

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    

    
print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test.txt"))
print(solve2(f"input/day{day}input.txt"))
