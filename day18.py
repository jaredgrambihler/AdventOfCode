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


def evalParts(parts):
    print(parts)
    if len(parts) == 1:
        return int(parts[0])
    try:
        firstParen = parts.index("(")
    except:
        firstParen = -1

    if firstParen >= 0:
        endParen = firstParen + 1
        depth = 0
        for part in parts[firstParen+1:]:
            if part == ")" and depth == 0:
                break
            elif part == "(":
                depth += 1
            elif part == ")":
                depth -= 1
            endParen += 1
        print(firstParen, endParen)
        return evalParts(parts[:firstParen] + [evalParts(parts[firstParen+1:endParen])] + parts[endParen +1:])

    # for part two I just changed this code
    # for part 1 we just check for a lower index and set the first value
    # to a very large number if not found
    try:
        firstPlus = parts.index("+")
    except:
        firstPlus = -1
    if firstPlus >= 0:
        result = int(parts[firstPlus-1]) + int(parts[firstPlus+1])
        return evalParts(parts[:firstPlus-1] + [result] + parts[firstPlus+2:])
    try:
        firstTimes = parts.index("*")
    except:
        firstTimes = -1
    if firstTimes >= 0:
        result = int(parts[firstTimes-1]) * int(parts[firstTimes+1])
        return evalParts(parts[:firstTimes-1] + [result] + parts[firstTimes+2:])

    print(f"Cannot evaluate expression {parts}")

def lineTotal(line):
    line = line.replace(" ", "")
    parts = [line[0]]
    for c in line[1:]:
        ops = set(["(", ")", "+", "*"])
        if c in ops:
            parts.append(c)
        elif parts[-1] in ops:
            parts.append(c)
        else:
            parts[-1] = parts[-1] + c
    return evalParts(parts)


def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    total= 0
    for line in text.splitlines():
        total += lineTotal(line)
    return total



print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))
