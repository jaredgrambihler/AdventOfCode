import copy
from pprint import pprint

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    lines = text.splitlines()
    startTime = int(lines[0])
    times = [int(x) for x in lines[1].split(",") if x != "x"]
    minLeaveTime = 9999999
    minBus = -1
    for time in times:
        cur = 0 
        while cur < startTime:
            cur += time
        
        if cur < minLeaveTime:
            minLeaveTime = cur
            minBus = time
    print(minLeaveTime, minBus)
    return (minLeaveTime - startTime) * minBus

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    lines = text.splitlines()
    startTime = int(lines[0])
    ids = [x for x in lines[1].split(",")]
    l = []
    for i, busId in enumerate(ids):
        if busId == "x":
            continue
        l.append((i, int(busId)))

    time = 0
    # start moving at a step of all multiples to satisfy
    stepSize = l[0][1]
    for offset, busId in l[1:]:
        # loop until offset is valid
        while (time + offset) % busId != 0:
            time += stepSize
        # have to satisfy both multiples when finding the next offset
        stepSize *= busId
    return time
   

print(solve2("input/day13test.txt"))
print(solve2("input/day13input.txt"))
