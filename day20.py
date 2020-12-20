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

    @staticmethod
    def flip(tile):
        new_tile = copy.deepcopy(tile.tile)
        for j in range(len(new_tile[0]) // 2):
            for i in range(len(new_tile)):
                new_tile[i][j], new_tile[i][-j-1] = new_tile[i][-j-1], new_tile[i][j]
        return Tile(tile.number, new_tile)


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


def combine_grid(tile_grid):
    combined = []
    for row in tile_grid:
        small_tiles = []
        for num, tile in row:
            small_tiles.append(tile.small_tile)
        cur_rows = [[] for _ in range(len(small_tiles[0]))]
        for small_tile in small_tiles:
            for i, row in enumerate(small_tile):
                cur_rows[i] += row
        combined += cur_rows
    return combined


def find_below(tile, tileNum, tiles, ingrid):
    edge = tile.bottom
    for other_num, other_tile in tiles.items():
        if other_num == tileNum or other_num in ingrid:
            continue
        for flip_way in [other_tile, Tile.flip(other_tile)]:
            for cur_tile in [Tile.rotate(flip_way, i) for i in range(0, 4)]:
                if cur_tile.top == edge:
                    return (other_num, cur_tile)

def find_right(tile, tileNum, tiles, ingrid):
    edge = tile.right
    for other_num, other_tile in tiles.items():
        if other_num == tileNum or other_num in ingrid:
            continue
        for flip_way in [other_tile, Tile.flip(other_tile)]:
            for cur_tile in [Tile.rotate(flip_way, i) for i in range(0, 4)]:
                if cur_tile.left == edge:
                    return (other_num, cur_tile)

def is_sea_monster(combined_grid, i, j):
    monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #
"""
    for x, line in enumerate(monster.splitlines()):
        for y, char in enumerate(line):
            if char == "#":
                if combined_grid[i+x][j+y] != "#":
                    return False
    return True

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    tiles = dict()
    cur_lines = []
    for tile_lines in text.split("\n\n"):
        tile_lines = tile_lines.splitlines()
        number = int(tile_lines[0].split()[1][:-1])
        tiles[number] = Tile(number, tile_lines[1:])
    
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
    top_left_tile = Tile.rotate(tiles[top_left], rotation_times[right_side])
    # find the matches in the rest of the tiles like we did before to build this out
    
    ingrid = set([top_left])
    first_row = [(top_left, top_left_tile)]
    while True:
        right_tile = find_right(first_row[-1][1], first_row[-1][0], tiles, ingrid)
        if not right_tile:
            break
        ingrid.add(right_tile[0])
        tiles[right_tile[0]] = right_tile[1]
        first_row.append(right_tile)

    tile_grid = [first_row]
    
    while True:
        below_tile = find_below(tile_grid[-1][0][1], tile_grid[-1][0][0], tiles, ingrid)
        if not below_tile:
            break
        ingrid.add(below_tile[0])
        tiles[below_tile[0]] = below_tile[1]
        row = [below_tile]
        while True:
            right_tile = find_right(row[-1][1], row[-1][0], tiles, ingrid)
            if not right_tile:
                break
            ingrid.add(right_tile[0])
            tiles[right_tile[0]] = right_tile[1]
            row.append(right_tile)
        tile_grid.append(row)

    print("Grid is")
    for x in tile_grid:
        print([y[0] for y in x])

    combined_grid = combine_grid(tile_grid)

    # look for sea monster
    # assume none overlap
    sea_monster_x = 20
    sea_monster_y = 3
    monster_counts = []
    for grid in [combined_grid, Tile.rotate(Tile(-1, combined_grid), 1).tile,
                 Tile.rotate(Tile(-1, combined_grid), 2).tile,
                 Tile.rotate(Tile(-1, combined_grid), 3).tile]:
        for flipped_grid in [grid, Tile.flip(Tile(-1, grid)).tile]:
            monsters = 0
            for i in range(len(flipped_grid) - sea_monster_y + 1):
                for j in range(len(flipped_grid[0]) - sea_monster_x + 1):
                    if is_sea_monster(flipped_grid, i, j):
                        monsters +=1
            monster_counts.append(monsters)
    print("Monster found", monster_counts)
    # use max count
    monsters = max(monster_counts)
    num_hashs = 0
    for i in range(len(combined_grid)):
        for j in range(len(combined_grid[0])):
            if combined_grid[i][j] == "#":
                num_hashs += 1
    monster_hash = 15
    print("Num hashes", num_hashs)
    return num_hashs - monster_hash * monsters

print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test.txt"))
print(solve2(f"input/day{day}input.txt"))
