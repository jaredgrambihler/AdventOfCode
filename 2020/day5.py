
def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    allSeats = []
    lineIds = []
    for line in text.splitlines():
        line = line.strip()
        if len(line) == 0:
            continue
        rowRange = (0, 127)
        for char in line[:8]:
            shrink  =(rowRange[1] - rowRange[0] + 1) // 2
            if char == 'F':
                rowRange = (rowRange[0], rowRange[1] - shrink)
            else:
                rowRange = (rowRange[0] + shrink,  rowRange[1])
        if line[7] == 'F':
            row = rowRange[0]
        else:
            row = rowRange[1]
        colRange = (0,7)

        for char in line[7:]:
            shrink  =(colRange[1] - colRange[0] + 1) // 2
            if char == 'L':
                colRange = (colRange[0], colRange[1] - shrink)
            else:
                colRange = (colRange[0] + shrink,  colRange[1])
            

        if line[-1] == 'L':
            col = colRange[0]
        else:
            col = colRange[1]
        if col == 2:
            print(line)
        lineId =row * 8 + col
        lineIds.append(lineId)
        allSeats.append((row, col))
    isSeat = [[False for _ in range(8)] for _ in range(128)]
    for seat in allSeats:
        isSeat[seat[0]][seat[1]] = True
    for i, row in enumerate(isSeat):
        for j, col in enumerate(row):
            if not col:
                pass
                print(i, j)
    return max(lineIds)

print(solve("input/day5test.txt"))
print(solve("input/day5input.txt"))

print(76 * 8 + 2)