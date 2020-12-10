import sys
import copy

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    l = [int(x) for x in text.splitlines() if x.strip() != ""]
    jolts = 0
    ones = 0
    threes = 0
    ways = 1
    joltl = [0]
    while l:
        nextVoltage = min(l)
        i = l.index(nextVoltage)
        del l[i]
        if nextVoltage  - jolts == 1:
            ones += 1
        elif nextVoltage  - jolts== 3:
            threes += 1
        jolts = nextVoltage
        joltl.append(jolts)
    return ones * (threes+1)


def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    l = [int(x) for x in text.splitlines() if x.strip() != ""]
    l.sort()
    l = [0] + l
    l = l + [l[-1] + 3]
    combinations = {0:1}
    for x in l[1:]:
        prev1 = combinations.get(x-1, 0)
        prev2 = combinations.get(x-2, 0)
        prev3 = combinations.get(x-3, 0)
        cur = prev1 + prev2 + prev3
        combinations[x] = cur
    return max(combinations.values())

print(solve2("input/day10test.txt"))
print(solve2("input/day10input.txt"))
