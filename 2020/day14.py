import copy
from pprint import pprint


def makeMask(mask):
   return [c for c in mask.strip()]

def intToBits(v):
    bits = [c for c in bin(v)[2:]]
    return ["0" for _ in range(64 - len(bits))] + bits
    

def applyMask(mask, bits):
    for i in range(1, len(mask)+1):
        if mask[-i] != "X":
            bits[-i] = mask[-i]
    return int("".join(bits), 2)


def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    lines = text.splitlines()
    mask = [c for c in lines[0].split("=")[1][1:]]
    memory = dict()
    for line in lines[1:]:
        parts = line.split("=")
        if parts[0].strip() == "mask":
            mask = makeMask(parts[1])
        else:
            memoryLoc = parts[0].strip().replace("mem", "").replace("[", "").replace("]", "")
            memoryLoc = int(memoryLoc)
            bits = intToBits(int(parts[1].strip()))
            value = applyMask(mask, bits)
            memory[memoryLoc] = value
    return sum(memory.values())
    
def makeCombinations(addressBits):
    combinations = [ [] ]
    for bit in addressBits:
        if bit == "1" or bit == "0":
            for x in combinations:
                x.append(bit)
        else:
            other_combinations = copy.deepcopy(combinations)
            for x in combinations:
                x.append("1")
            for x in other_combinations:
                x.append("0")
            combinations = combinations + other_combinations
    return [int("".join(bits), 2) for bits in combinations]

def findAddresses(mask, addressBits):
    for i in range(1, len(mask)+1):
        if mask[-i] == "X" or mask[-i] == "1":
            addressBits[-i] = mask[-i]
    return makeCombinations(addressBits)

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    lines = text.splitlines()
    mask = [c for c in lines[0].split("=")[1][1:]]
    memory = dict()
    for line in lines[1:]:
        parts = line.split("=")
        if parts[0].strip() == "mask":
            mask = makeMask(parts[1])
        else:
            memoryLoc = parts[0].strip().replace("mem", "").replace("[", "").replace("]", "")
            memoryLoc = int(memoryLoc)
            value = int(parts[1].strip())
            addressBits = intToBits(memoryLoc)
            addresses = findAddresses(mask, addressBits)
            for address in addresses:
                memory[address] = value
    return sum(memory.values())

print("Part 1")
print(solve("input/day14test.txt"))
print(solve("input/day14input.txt"))

print("Part 2")
print(solve2("input/day14test2.txt"))
print(solve2("input/day14input.txt"))