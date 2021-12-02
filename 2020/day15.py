import copy
import matplotlib.pyplot as plt
from pprint import pprint

def solveBoth(inputF, sequenceNumber):
    with open(inputF, 'r') as f:
        text = f.read()
    nums = [int(x) for x in text.split(",")]
    sequenceVals = copy.copy(nums)
    # start of speaking
    numToSpoken = {num: i for i, num in enumerate(nums[:-1])}
    cur = nums[-1]
    for i in range(len(nums)-1, sequenceNumber - 1):
        if cur not in numToSpoken:
            nextVal = 0
        else:
            nextVal = i - numToSpoken[cur]
        numToSpoken[cur] = i
        cur = nextVal
        sequenceVals.append(cur)
    plt.plot([x for x in range(sequenceNumber)], sequenceVals)
    plt.show
    return cur

def solve(inputF):
    return solveBoth(inputF, 2020)


def solve2(inputF):
    return solveBoth(inputF, 30000000)
    

print("Part 1")
print(solve("input/day15test.txt"))
print(solve("input/day15input.txt"))

print("Part 2")
print(solve2("input/day15test.txt"))
print(solve2("input/day15input.txt"))