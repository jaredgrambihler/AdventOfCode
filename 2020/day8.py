import sys
import copy

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    accum = 0
    instr = 0
    instructions = []
    for line in text.splitlines():
        line = line.strip()
        if line == "":
            continue
        words = line.split()
        instructions.append((words[0], words[1]))
    print(instructions)
    executed = [False for _ in range(len(instructions))]
    while True:
        if instr == len(instructions):
            print(f"Terminated with value {accum}")
            sys.exit()
        if executed[instr]:
            return accum
        executed[instr] = True
        command, val = instructions[instr]
        if command == "nop":
            instr += 1
            continue
        elif command == "acc":
            if val[0] == "-":
                accum -= int(val[1:])
            else:
                accum += int(val[1:])
            instr += 1
            continue
        elif command == "jmp":
            if val[0] == "-":
                instr -= int(val[1:])
            else:
                instr += int(val[1:])
        else:
            print(f"unknown command {command}")

def attempt(instructions):
    accum = 0
    instr = 0
    executed = [False for _ in range(len(instructions))]
    while True:
        if instr == len(instructions):
            print(f"Terminated with value {accum}")
            sys.exit()
        if executed[instr]:
            return accum
        executed[instr] = True
        command, val = instructions[instr]
        if command == "nop":
            instr += 1
            continue
        elif command == "acc":
            if val[0] == "-":
                accum -= int(val[1:])
            else:
                accum += int(val[1:])
            instr += 1
            continue
        elif command == "jmp":
            if val[0] == "-":
                instr -= int(val[1:])
            else:
                instr += int(val[1:])
        else:
            print(f"unknown command {command}")

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    accum = 0
    instr = 0
    instructions = []
    for line in text.splitlines():
        line = line.strip()
        if line == "":
            continue
        words = line.split()
        instructions.append((words[0], words[1]))
    for i in range(len(instructions)):
        temp = copy.copy(instructions)
        if instructions[i][0] == "acc":
            continue
        elif instructions[i][0] == "nop":
            temp[i] = ("jmp", instructions[i][1])
        elif instructions[i][0] == "jmp":
            temp[i] = ("nop", instructions[i][1])
        else:
            print(f"unknown command {instructions[i][0]}")
        attempt(temp)

print(solve("input/day8test.txt"))
print(solve("input/day8input.txt"))