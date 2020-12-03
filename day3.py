with open("day3input.txt", "r") as f:
    inputLines = f.read().splitlines()

def isTree(i, j):
    lineLength = len(inputLines[0])
    j = j % lineLength
    return inputLines[i][j] == "#"


def treesOnSlope(y, x):
    i = 0
    j = 0
    trees = 0
    while i < len(inputLines):
        if isTree(i, j):
            trees += 1
        i += x
        j += y
    return trees

print(treesOnSlope(3, 1))

total = 1
for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    total *= treesOnSlope(slope[0], slope[1])

print(total)