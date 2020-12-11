import sys
import copy
from pprint import pprint

def update(seats):
    nextSeats = copy.deepcopy(seats)
    for i in range(len(nextSeats)):
        for j in range(len(nextSeats[0])):
            # check the seat count
            if seats[i][j] == ".":
                continue
            count = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if k == i and j == l:
                        continue
                    if k < 0 or l < 0 or k >= len(seats) or l >= len(seats[0]):
                        continue
                    if seats[k][l] == "#":
                        count +=1
            if count >= 4:
                nextSeats[i][j] = "L"
            elif count == 0:
                nextSeats[i][j] = "#"
    # pprint(nextSeats)
    return nextSeats

def above(seats, i , j):
    i -= 1
    while i >= 0:
        if seats[i][j] == "L":
            return False
        elif seats[i][j] == "#":
            return True
        i -= 1
    return False

def below(seats, i , j):
    i += 1
    while i < len(seats):
        if seats[i][j] == "L":
            return False
        elif seats[i][j] == "#":
            return True
        i += 1
    return False

def left(seats, i , j):
    j -= 1
    while j >= 0:
        if seats[i][j] == "L":
            return False
        elif seats[i][j] == "#":
            return True
        j -= 1
    return False

def right(seats, i , j):
    j += 1
    while j < len(seats[0]):
        if seats[i][j] == "L":
            return False
        elif seats[i][j] == "#":
            return True
        j += 1
    return False

def upleft(seats, i , j):
    i -= 1
    j -= 1
    while i >= 0 and j >= 0:
        if seats[i][j] == "L":
            return False
        elif seats[i][j] == "#":
            return True
        i -= 1
        j -= 1
    return False

def upright(seats, i , j):
    i -= 1
    j += 1
    while i >= 0 and j < len(seats[0]):
        if seats[i][j] == "L":
            return False
        elif seats[i][j] == "#":
            return True
        i -= 1
        j += 1
    return False

def downleft(seats, i , j):
    i += 1
    j -= 1
    while i < len(seats) and j >= 0:
        if seats[i][j] == "L":
            return False
        elif seats[i][j] == "#":
            return True
        j -= 1
        i += 1
    return False

def downright(seats, i , j):
    i += 1
    j += 1
    while i < len(seats) and j < len(seats[0]):
        if seats[i][j] == "L":
            return False
        elif seats[i][j] == "#":
            return True
        i += 1 
        j += 1
    return False

def update2(seats):
    nextSeats = copy.deepcopy(seats)
    for i in range(len(nextSeats)):
        for j in range(len(nextSeats[0])):
            # check the seat count
            if seats[i][j] == ".":
                continue
            count = 0
            if above(seats, i, j):
                count +=1 
            if below(seats, i, j):
                count += 1
            if left(seats, i, j):
                count += 1
            if right(seats, i , j):
                count +=1
            if upleft(seats, i, j):
                count += 1
            if upright(seats, i, j):
                count += 1
            if downleft(seats, i, j):
                count += 1
            if downright(seats, i, j):
                count += 1
            if count >= 5:
                nextSeats[i][j] = "L"
            elif count == 0:
                nextSeats[i][j] = "#"
    # pprint(nextSeats)
    return nextSeats


def countseats(seats):
    occupied = 0
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == "#":
                occupied +=1 
    return occupied

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    seats = [[c for c in x] for x in text.splitlines()]
    prev = []
    while prev != seats:
        prev = seats
        seats = update(seats)
    return countseats(seats)
    

def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    seats = [[c for c in x] for x in text.splitlines()]
    prev = []
    while prev != seats:
        prev = seats
        seats = update2(seats)
    return countseats(seats)

print(solve2("input/day11test.txt"))
print(solve2("input/day11input.txt"))
