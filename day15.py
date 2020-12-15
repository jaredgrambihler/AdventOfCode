import copy
from pprint import pprint

def solveBoth(inputF, sequenceNumber):
    with open(inputF, 'r') as f:
        text = f.read()
    nums = [int(x) for x in text.split(",")]
    # start of speaking
    numToSpoken = {num: i for i, num in enumerate(nums[:-1])}
    prev = nums[-1]
    for i in range(len(nums)-1, sequenceNumber - 1):
        if prev not in numToSpoken:
            cur = 0
        else:
            cur = i - numToSpoken[prev]
        numToSpoken[prev] = i
        prev = cur
    return prev

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