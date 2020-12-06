from collections import Counter

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    groups = []
    group = ""
    for line in text.splitlines():
        if line.strip() == "":
            groups.append(group)
            group = ""
        else:
            group += " " + line
    total = 0
    for group in groups:
        if group.strip() == "":
            continue
        answers = group.split(" ")
        s = set(char for char in answers[1])
        for answer in answers[1:]:
            answerChars = set([char for char in answer])
            s = s.intersection(answerChars)
        total += len(s)

    return total

print(solve("input/day6test.txt"))
print(solve("input/day6input.txt"))