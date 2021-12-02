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
        while i < len(line):
            if line[i] == 's' or line[i] == 'n':
                directions.append(line[i] + line[i+1])
                i += 2
            elif line[i] == 'e' or line[i] == 'w':
                directions.append(line[i])
                i += 1
            else:
                print("Not possible")
        all_directions.append(directions)
    black_tiles = set()
    c = Counter()
    for directions in all_directions:
        x = 0
        y = 0
        z = 0
        for direction in directions:
            if direction == "e":
                y -= 1
                x += 1
            elif direction == "w":
                y += 1
                x -= 1
            elif direction == "nw":
                x -=1
                z += 1
            elif direction == "ne":
                y -= 1
                z += 1
            elif direction == "sw":
                y += 1
                z -= 1
            elif direction == "se":
                x += 1
                z -= 1
            else:
                print("not possible")
        tile = (x, y, z)
        c[tile] += 1
        if tile in black_tiles:
            # flip back to white if it is black
            black_tiles.remove(tile)
        else:
            # make it black
            black_tiles.add(tile)
    return len(black_tiles)

def adj_to(tile):
    x, y, z = tile
    return [(x-1, y, z+1), (x, y-1, z+1), (x+1, y-1, z), (x+1, y, z-1), (x, y+1, z-1), (x-1, y+1, z)]

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    all_directions = []
    for line in text.splitlines():
        directions = []
        i = 0
        while i < len(line):
            if line[i] == 's' or line[i] == 'n':
                directions.append(line[i] + line[i+1])
                i += 2
            elif line[i] == 'e' or line[i] == 'w':
                directions.append(line[i])
                i += 1
            else:
                print("Not possible")
        all_directions.append(directions)
    black_tiles = set()
    c = Counter()
    for directions in all_directions:
        x = 0
        y = 0
        z = 0
        for direction in directions:
            if direction == "e":
                y -= 1
                x += 1
            elif direction == "w":
                y += 1
                x -= 1
            elif direction == "nw":
                x -=1
                z += 1
            elif direction == "ne":
                y -= 1
                z += 1
            elif direction == "sw":
                y += 1
                z -= 1
            elif direction == "se":
                x += 1
                z -= 1
            else:
                print("not possible")
        tile = (x, y, z)
        c[tile] += 1
        if tile in black_tiles:
            # flip back to white if it is black
            black_tiles.remove(tile)
        else:
            # make it black
            black_tiles.add(tile)

    for _ in range(100):
        next_black_tiles = set()
        for tile in black_tiles:
            adj = 0
            for other in adj_to(tile):
                if other in black_tiles:
                    adj += 1
            if adj == 1 or adj == 2:
                next_black_tiles.add(tile)
        # look for white tiles
        while_tiles = Counter()
        for tile in black_tiles:
            for other in adj_to(tile):
                if other in black_tiles:
                    continue
                else:
                    while_tiles[other] += 1
        for tile, count in while_tiles.items():
            if count == 2:
                next_black_tiles.add(tile)
        black_tiles = next_black_tiles
    return len(black_tiles)

    
print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test.txt"))
print(solve2(f"input/day{day}input.txt"))
