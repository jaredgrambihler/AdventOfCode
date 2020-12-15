import copy
from pprint import pprint

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    nums = [int(x) for x in text.split(",")]
    # start of speaking
    numToSpoken = {num: i for i, num in enumerate(nums[:-1])}
    prev = nums[-1]
    for i in range(len(nums)-1, 2019):
        if prev not in numToSpoken:
            nextVal = 0
            numToSpoken[prev] = i
            prev = nextVal
        else:
            cur = i - numToSpoken[prev]
            numToSpoken[prev] = i
            prev = cur
        # print(prev, numToSpoken)
    return prev
    

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    nums = [int(x) for x in text.split(",")]
    # start of speaking
    numToSpoken = {num: i for i, num in enumerate(nums[:-1])}
    prev = nums[-1]
    for i in range(len(nums)-1, 30000000-1):
        if prev not in numToSpoken:
            nextVal = 0
            numToSpoken[prev] = i
            prev = nextVal
        else:
            cur = i - numToSpoken[prev]
            numToSpoken[prev] = i
            prev = cur
    return prev
    

print("Part 1")
print(solve("input/day15test.txt"))
print(solve("input/day15input.txt"))

print("Part 2")
print(solve2("input/day15test.txt"))
print(solve2("input/day15input.txt"))