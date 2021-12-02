
def hasSum(val, numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == val:
                return True
    return False

def solve2(val, numbers, i):
    del numbers[i]
    for size in range(len(numbers)):
        for start in range(len(numbers)):
            if sum(numbers[start:start+size]) == val:
                print(f"Range: {numbers[start:start+size]}")
                return min(numbers[start:start+size]) + max(numbers[start:start+size])
    return 0


def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    lines = [int(x.strip()) for x in text.splitlines() if x.strip != ""]
    preamble = 25
    lastWords = []
    for i in range(preamble):
        lastWords.append(lines[i])
    for i in range(preamble, len(lines)):
        if not hasSum(lines[i], lastWords):
            rangeNumbers = solve2(lines[i], lines, i)
            return rangeNumbers
        lastWords = lastWords[1:] + [lines[i]]


# print(solve("input/day9test.txt"))
print(solve("input/day9input.txt"))