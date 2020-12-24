import copy
import os
import re
import sys
from collections import Counter
import numpy as np
from pprint import pprint

try:
    day = re.findall("\d+", os.path.basename(__file__))[0]
except IndexError:
    print("No day in file")
    sys.exit()


def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    cups = [int(c) for c in text]
    i = 0
    cur = cups[-1]
    minCup = min(cups)
    maxCup = max(cups)
    for _ in range(100):
        cur = cups[(cups.index(cur) + 1) % len(cups)]
        i = cups.index(cur)
        next_3_indexes = [ (i + 1) % len(cups), (i + 2) % len(cups), (i + 3) % len(cups)]
        next_3 = [cups[x] for x in next_3_indexes]
        destination_cup = cur - 1
        for index in sorted(next_3_indexes, reverse=True):
            del cups[index]
        while True:
            if destination_cup < minCup:
                destination_cup = maxCup
            if destination_cup in cups:
                # found it
                index = cups.index(destination_cup)
                cups = cups[:index+1] + next_3 + cups[index+1:]
                break
            destination_cup -= 1
        i += 1
    
    print(cups)
    one_index = cups.index(1)
    cups = cups[one_index:] + cups[:one_index]
    return "".join(str(x) for x in cups[1:])


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prior = None

    def __hash__(self):
        return self.val*2654435761 % 2^32

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    cups = [int(c) for c in text]
    i = 0
    cur = cups[-1]
    maxCup = max(cups)
    cups = cups + [x for x in range(maxCup + 1, 1000000 + 1)]
    minCup = min(cups)
    maxCup = max(cups)
    # make a linked list
    head = Node(cups[0])
    cur = head
    for cup in cups[1:]:
        temp = Node(cup)
        cur.next = temp
        temp.prior = cur
        cur = temp
    cur.next = head

    cupToNode = dict()
    cupToNode[head.val] = head
    cur = head.next
    while(cur != head):
        cupToNode[cur.val] = cur
        cur = cur.next

    cur = head
    for _ in range(10000000):
        next_3 = [cur.next, cur.next.next, cur.next.next.next]
        cur.next = next_3[-1].next
        cur.next.prior = cur
        destination_value = cur.val - 1
        while True:
            if destination_value < minCup:
                destination_value = maxCup
            if destination_value in cupToNode and cupToNode[destination_value] not in next_3:
                # found it
                node = cupToNode[destination_value]
                temp = node.next
                
                node.next = next_3[0]
                next_3[0].prior = node
                next_3[-1].next = temp
                temp.prior = next_3[-1]
                break
            destination_value -= 1
        cur = cur.next

    # find 1 cup
    return cupToNode[1].next.val * cupToNode[1].next.next.val

    
print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test.txt"))
print(solve2(f"input/day{day}input.txt"))
