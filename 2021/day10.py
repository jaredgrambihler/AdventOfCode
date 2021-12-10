with open("input/day10input.txt") as f:
    input_text = f.read()

lines = input_text.strip().splitlines()

bracket_to_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

open_to_close = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

def get_corrupted_score(lines):
    score = 0
    for line in lines:
        line = line.strip()
        open_stack = []
        for c in line:
            if c in open_to_close:
                open_stack.append(c)
            else:
                # must be closing
                # if stack is empty, can't be a wrong close
                if len(open_stack) > 1:
                    correct_close = open_to_close[open_stack.pop()]
                    if correct_close != c:
                        score += bracket_to_score[c]
    return score


bracket_to_completion_score = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def get_completion_score(lines):
    scores = []
    for line in lines:
        line = line.strip()
        open_stack = []
        corrupt = False
        for c in line:
            if c in open_to_close:
                open_stack.append(c)
            elif len(open_stack) > 1:
                correct_close = open_to_close[open_stack.pop()]
                if correct_close != c:
                    corrupt = True
        if not corrupt:
            # open stack contains elements that need to be close
            # get the score
            cur_score = 0
            while len(open_stack) > 0:
                cur_score *= 5
                close = open_to_close[open_stack.pop()]
                close_score = bracket_to_completion_score[close]
                cur_score += close_score
            scores.append(cur_score)
    scores = sorted(scores)
    return scores[len(scores) // 2]


print("Part 1")
print(f"Corrupted score {get_corrupted_score(lines)}")
print("Part 2")
print(f"Completion score {get_completion_score(lines)}")
