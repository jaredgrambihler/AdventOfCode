import sys
import copy
from pprint import pprint

"""
  N
W   E
  S
"""
def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    l = text.splitlines()
    direction = 90 # east
    x = 0
    y = 0
    for line in l:
        letter, val = line[0], int(line[1:])
        if letter == "F":
            if direction == 0:
                letter = "N"
            elif direction == 90:
                letter = "E"
            elif direction == 180:
                letter = "S"
            elif direction == 270:
                letter = "W"
            else:
                print(f"unknown direction {direction}")

        if letter == "N":
            y += val
        elif letter == "S":
            y -= val
        elif letter == "E":
            x += val
        elif letter == "W":
            x -= val
        elif letter == "L":
            direction -= val
            direction = direction % 360
            if direction < 0:
                direction += 360
        elif letter == "R":
            direction += val
            direction = direction % 360
            if direction < 0:
                direction += 360

    return abs(x) + abs(y)

def rotateCounter(coords):
    x = coords[0]
    y = coords[1]
    return (-y, x)

def rotateClock(coords):
    x = coords[0]
    y = coords[1]
    return (y, -x)

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    l = text.splitlines()
    wayCoords = (10, 1)
    x = 0
    y = 0
    for line in l:
        letter, val = line[0], int(line[1:])
        if letter == "F":
            x += wayCoords[0] * val
            y += wayCoords[1] * val

        if letter == "N":
            wayCoords = (wayCoords[0], wayCoords[1] + val)
        elif letter == "S":
            wayCoords = (wayCoords[0], wayCoords[1] - val)
        elif letter == "E":
            wayCoords = (wayCoords[0] + val, wayCoords[1])
        elif letter == "W":
            wayCoords = (wayCoords[0] - val, wayCoords[1])
        elif letter == "L":
            times = val // 90
            assert (val / 90 == times)
            for time in range(times):
                wayCoords = rotateCounter(wayCoords)
        elif letter == "R":
            times = val // 90
            assert (val / 90 == times)
            for time in range(times):
               wayCoords = rotateClock(wayCoords)

    return abs(x) + abs(y)


print(solve2("input/day12test.txt"))
print(solve2("input/day12input.txt"))
