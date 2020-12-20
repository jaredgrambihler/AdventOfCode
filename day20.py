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

class Tile:

    def __init__(self, number, lines):
        self.number = number
        self.tile = [[c for c in line] for line in lines]
        self.rotation = 0

    def __str__(self):
        return "\n".join(["".join(c for c in line) for line in self.tile])

    def __repr__(self):
        return self.__str__()

    @property
    def top(self):
        return "".join(self.tile[0])

    @property
    def right(self):
        s = ""
        for line in self.tile:
            s += line[-1]
        return s

    @property
    def left(self):
        s = ""
        for line in self.tile:
            s += line[0]
        return s

    @property
    def bottom(self):
        return "".join(self.tile[-1])

    @property
    def small_tile(self):
        small = []
        for row in self.tile[1:-1]:
            small.append(row[1:-1])
        return small

    @staticmethod
    def rotate(tile, times = 1):
        number = tile.number
        tile = copy.deepcopy(tile.tile)
        tile = np.array(tile)
        for time in range(times):
            tile = np.rot90(tile)
        return Tile(number, tile)


def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    tiles = dict()
    cur_lines = []
    for tile_lines in text.split("\n\n"):
        tile_lines = tile_lines.splitlines()
        number = int(tile_lines[0].split()[1][:-1])
        tiles[number] = Tile(number, tile_lines[1:])

        # print(tile_lines)
        t = tiles[number]
        # print(f"Top: {t.top}\nLeft: {t.left}\nRight: {t.right}\nBottom: {t.bottom}")
    
    tile_to_adj = {(str(num) + d): [] for num in tiles.keys() for d in ["T", "L", "R", "B"]}

    tile_to_adj_reduce = {num: [] for num in tiles.keys()}

    for tileNum, tile in tiles.items():
        for other_tilenum, other_tile in tiles.items():
            if tileNum == other_tilenum:
                continue
            for pos, letter in zip([tile.top, tile.left, tile.right, tile.bottom] , ["T", "L", "R", "B"]):
                for other_pos, other_letter in zip([other_tile.top, other_tile.left, other_tile.right, other_tile.bottom] , ["T", "L", "R", "B"]):
                    if pos == other_pos or "".join(reversed(pos)) == other_pos:
                        tile_to_adj[str(tileNum) + letter].append(str(other_tilenum) + other_letter)
                        tile_to_adj_reduce[tileNum].append(other_tilenum)

    # a corner has EXACTLY 2 edges
    c = Counter()
    product = 1
    count = 0
    for k, v in tile_to_adj_reduce.items():
        if len(v) == 2:
            count +=1 
            product *= k
    # assert we only find 4 corners because this solution is super hacky
    assert count == 4
    return product


def combine_grid(tile_grid, tiles):
    combined = []
    for row in tile_grid:
        small_tiles = []
        for tile, rotation in row:
            tile = Tile.rotate(tiles[tile], rotation)
            small_tiles.append(tile.small_tile)
        cur_rows = [[] for _ in range(len(small_tiles[0]))]
        for small_tile in small_tiles:
            for i, row in enumerate(small_tile):
                cur_rows[i] += row
        combined += cur_rows
    return combined


def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    tiles = dict()
    cur_lines = []
    for tile_lines in text.split("\n\n"):
        tile_lines = tile_lines.splitlines()
        number = int(tile_lines[0].split()[1][:-1])
        tiles[number] = Tile(number, tile_lines[1:])

        # print(tile_lines)
        t = tiles[number]
        # print(f"Top: {t.top}\nLeft: {t.left}\nRight: {t.right}\nBottom: {t.bottom}")
    
    tile_to_adj = {(str(num) + d): [] for num in tiles.keys() for d in ["T", "L", "R", "B"]}

    tile_to_adj_reduce = {num: [] for num in tiles.keys()}
    flipped_tiles = set()
    for tileNum, tile in tiles.items():
        for other_tilenum, other_tile in tiles.items():
            if tileNum == other_tilenum:
                continue
            for pos, letter in zip([tile.top, tile.left, tile.right, tile.bottom] , ["T", "L", "R", "B"]):
                for other_pos, other_letter in zip([other_tile.top, other_tile.left, other_tile.right, other_tile.bottom] , ["T", "L", "R", "B"]):
                    if pos == other_pos or "".join(reversed(pos)) == other_pos:
                        tile_to_adj[str(tileNum) + letter].append(str(other_tilenum) + other_letter)
                        tile_to_adj_reduce[tileNum].append(other_tilenum)


    # start at a corner and grow the grid
    corners = []
    count = 0
    for k, v in tile_to_adj_reduce.items():
        if len(v) == 2:
            count +=1 
            corners.append(k)
    # assert we only find 4 corners because this solution is super hacky
    assert count == 4

    # check we can be naive and just add tiles as we see them
    for tile_side, adj in tile_to_adj.items():
        assert len(adj) <= 1

    side_to_num = {"T": 0, "R": 1, "B": 2, "L": 3}
    top_left = corners[0]
    corner_sides = []
    for side in ["T", "L", "R", "B"]:
        if tile_to_adj[str(top_left) + side]:
            corner_sides.append(side)
    corner_sides = sorted(corner_sides, key=lambda x: side_to_num[x])
    right_side = corner_sides[0]
    rotation_times = {"T": 3, "R": 0, "B": 1, "L": 2}
    # top_left_tile = Tile.rotate(tiles[top_left], rotation_times[right_side])
    
    
    def get_right_side(num, times):
        if times == 0:
            side = "R"
        elif times == 1:
            side = "B"
        elif times == 2:
            side = "L"
        elif times == 3:
            side = "T"
        return str(num) + side

    def get_bottom_side(num, times):
        side = ""
        if times == 0:
            side = "B"
        elif times == 1:
            side = "L"
        elif times == 2:
            side = "T"
        elif times == 3:
            side = "R"
        return str(num) + side


    tile_grid = [[]]
    
    count = 0
    print(tile_to_adj)
    while True:
        if count > 0:
            next_tile = tile_to_adj[get_bottom_side(tile_grid[-1][0][0], tile_grid[-1][0][1])]
            if len(next_tile) == 0:
                break
            next_tile = next_tile[0]
            side = next_tile[-1]
            num = int(next_tile[:-1])
            if side == "T":
                rotation = 0
            elif side == "R":
                rotation = 1
            elif side == "B":
                rotation = 2
            elif side == "L":
                rotation = 3
            row = []
            row.append((num, rotation))
        else:
            row  = [(top_left, rotation_times[right_side])]
        
        # get the first row tile
        while True:
            next_tile = tile_to_adj[get_right_side(row[-1][0], row[-1][1])]
            if len(next_tile) == 0:
                break
            next_tile = next_tile[0]
            side = next_tile[-1]
            num = int(next_tile[:-1])
            if side == "L":
                rotation = 0
            elif side == "T":
                rotation = 1
            elif side == "R":
                rotation = 2
            elif side == "B":
                rotation = 3
            row.append((num, rotation))
        tile_grid.append(row)
        count += 1
    tile_grid = tile_grid[1:]
    print("Tile Grid Rows")
    for row in tile_grid:
        print(len(row))

    value_grid = combine_grid(tile_grid, tiles)
    # for row in value_grid:
    #     print(len(row))
    # pprint(value_grid)

print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test.txt"))
# print(solve2(f"input/day{day}input.txt"))
