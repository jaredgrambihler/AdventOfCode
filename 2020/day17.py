"""This is code is awful but it works :) """
import copy
import os
import re
import sys
from pprint import pprint

try:
    day = re.findall("\d+", os.path.basename(__file__))[0]
except IndexError:
    print("No day in file")
    sys.exit()

def countNeighbors(point, points):
    x = point[0]
    y = point[1]
    z = point[2]
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if i == x and y==j and k==z:
                    continue
                if (i, j, k) in points and points[(i, j, k)] == "#":
                    count += 1
    return count

def cycle(points):
    nextPoints = copy.deepcopy(points)
    minX = 0
    maxX = 0
    minY = 0 
    maxY = 0
    minZ = 0
    maxZ = 1
    for point in points.keys():
        x = point[0]
        y = point[1]
        z = point[2]
        if x < minX:
            minX = x
        elif x > maxX:
            maxX = x
        if y < minY:
            minY = y
        elif y > maxY:
            maxY = y
        if z < minZ:
            minZ = z
        elif z > maxZ:
            maxZ = z
    print(minX, maxX, minY, maxY, minZ, maxZ)
    for i in range(minX-1, maxX + 2):
        for j in range(minY-1, maxY + 2):
            for k in range(minZ-1, maxZ + 2):
                point = (i, j, k)
                count = countNeighbors((i, j, k), points)
                val = points.get((i, j, k), ".")
                if not (val == "#" and count ==2 or count == 3):
                    nextPoints[point] = "."
                elif (val == "." and count == 3):
                    nextPoints[point] = "#"
                else:
                    nextPoints[point] = val
    return nextPoints
        

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    points = dict()
    for i, line in enumerate(text.splitlines()):
        for j, point in enumerate(line):
            points[(i, j, 0)] = point
    for i in range(6):
        points = cycle(points)

    count = 0
    for x in points.values():
        if x == "#":
            count += 1
    return count



def countNeighbors2(point, points):
    x = point[0]
    y = point[1]
    z = point[2]
    w = point[3]
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    if i == x and y==j and k==z and l == w:
                        continue
                    if (i, j, k, l) in points and points[(i, j, k, l)] == "#":
                        count += 1
    return count

def cycle2(points):
    nextPoints = copy.deepcopy(points)
    minX = 0
    maxX = 0
    minY = 0 
    maxY = 0
    minZ = 0
    maxZ = 1
    minW = 0
    maxW = 1
    for point in points.keys():
        x = point[0]
        y = point[1]
        z = point[2]
        w = point[3]
        if x < minX:
            minX = x
        elif x > maxX:
            maxX = x
        if y < minY:
            minY = y
        elif y > maxY:
            maxY = y
        if z < minZ:
            minZ = z
        elif z > maxZ:
            maxZ = z
        if w < minW:
            minW = w
        elif w > maxW:
            maxW = w
    print(minX, maxX, minY, maxY, minZ, maxZ, minW, maxW)
    for i in range(minX-1, maxX + 2):
        for j in range(minY-1, maxY + 2):
            for k in range(minZ-1, maxZ + 2):
                for l in range(minW -1 , maxW + 2):
                    point = (i, j, k, l)
                    count = countNeighbors2(point, points)
                    val = points.get(point, ".")
                    if not (val == "#" and count ==2 or count == 3):
                        nextPoints[point] = "."
                    elif (val == "." and count == 3):
                        nextPoints[point] = "#"
                    else:
                        nextPoints[point] = val
    return nextPoints



def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    points = dict()
    for i, line in enumerate(text.splitlines()):
        for j, point in enumerate(line):
            points[(i, j, 0, 0)] = point
    print(points)
    for i in range(6):
        points = cycle2(points)

    count = 0
    for x in points.values():
        if x == "#":
            count += 1
    return count

    

print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test.txt"))
print(solve2(f"input/day{day}input.txt"))
