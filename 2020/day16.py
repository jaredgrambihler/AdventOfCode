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

def inARange(field, allRanges):
    for lower, upper in allRanges:
        if field >= lower and field <= upper:
            return True
    return False

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    sections = text.split("\n\n")
    rules = dict()
    for line in sections[0].splitlines():
        parts = line.split(":")
        name = parts[0].strip()
        ranges = parts[1].strip().split("or")
        ranges = [x.split("-") for x in ranges]
        ranges = [(int(x[0]), int(x[1])) for x in ranges]
        rules[name] = ranges

    yourTicket = sections[1].splitlines()[1]
    yourTicket = [int(x) for x in yourTicket.split(",")]

    allRanges = []
    for rangeList in rules.values():
        allRanges += rangeList

    invalidValues = []
    for line in sections[2].splitlines()[1:]:
        ticket = [int(x) for x in line.split(",")]
        for field in ticket:
            if not inARange(field, allRanges):
                invalidValues.append(field)
    
    return sum(invalidValues)
        

def findPositionsFromValid(validForPosition):
    validForPosition = copy.deepcopy(validForPosition)
    while not all(len(x) == 1 for x in validForPosition):
        valid_once = set()
        for pos_valid in validForPosition:
            if len(pos_valid) == 1:
                valid_once.add(pos_valid[0])
        
        for pos_valid in validForPosition:
            if len(pos_valid) == 1:
                continue
            for valid in pos_valid:
                if valid in valid_once:
                    pos_valid.remove(valid)

    return validForPosition

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    sections = text.split("\n\n")
    rules = dict()
    for line in sections[0].splitlines():
        parts = line.split(":")
        name = parts[0].strip()
        ranges = parts[1].strip().split("or")
        ranges = [x.split("-") for x in ranges]
        ranges = [(int(x[0]), int(x[1])) for x in ranges]
        rules[name] = ranges

    yourTicket = sections[1].splitlines()[1]
    yourTicket = [int(x) for x in yourTicket.split(",")]

    allRanges = []
    for rangeList in rules.values():
        allRanges += rangeList

    invalidValues = []
    allTickets = []
    for line in sections[2].splitlines()[1:]:
        ticket = [int(x) for x in line.split(",")]
        validTicket = True
        for field in ticket:
            if not inARange(field, allRanges):
                validTicket = False
        if validTicket:
            allTickets.append(ticket)
    
    validForPosition = [ [] for _ in range(len(yourTicket))]
    for i in range(len(yourTicket)):
        valid_for_i = []
        for name, ranges in rules.items():
            validName = True
            for ticket in allTickets + [yourTicket]:
                if not inARange(ticket[i], ranges):
                    validName = False
                    break
            if validName:
                valid_for_i.append(name)
        validForPosition[i] = valid_for_i
    
    positionNames = findPositionsFromValid(validForPosition)
    print(positionNames)
    
    value = 1
    for i in range(len(positionNames)):
        print(positionNames[i])
        if "departure" in positionNames[i][0]:
            print(yourTicket[i])
            value *= yourTicket[i]
    return value

print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test.txt"))
print(solve2(f"input/day{day}input.txt"))