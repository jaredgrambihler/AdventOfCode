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

print(solve("input/day10test.txt"))
print(solve("input/day10input.txt"))
