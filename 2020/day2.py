import re

with open("input/day2input.txt", "r") as f:
    inputlines = f.read().splitlines()

validPasswords = 0
validOtherRule = 0
for line in inputlines:
    lineParts = re.split(r"[\-: ]", line)
    lowBound = int(lineParts[0])
    highBound = int(lineParts[1])
    letter = lineParts[2]
    password = lineParts[-1]
    count = 0
    for c in password:
        if c == letter:
            count += 1
    if count >= lowBound and count <= highBound:
        validPasswords += 1
    if password[lowBound - 1] == letter or password[highBound - 1] == letter:
        if password[lowBound - 1] != password[highBound - 1]:
            validOtherRule += 1

print(validPasswords)
print(validOtherRule)