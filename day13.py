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

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

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
    i = 0
    print(l)
    dp = [0 for _ in range(len(l))]
    dp[0] = l[0][1]
    stepSize = l[0][1]
    for i in range(1, len(dp)):
        prevValue = dp[i-1]
        offset = (prevValue % l[i][1]) - l[i][0]
        while offset != 0:
            prevValue += stepSize
            offset = (prevValue % l[i][1]) - l[i][0]
        dp[i] = prevValue
        stepSize = lcm(dp[i], dp[i-1])
        print(dp)
    return dp[-1]
    
    

    
   

print(solve2("input/day13test.txt"))
# print(solve2("input/day13input.txt"))
