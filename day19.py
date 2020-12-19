import copy
import os
import re
import sys
from pprint import pprint

try:
    day = re.findall("\d+", os.path.basename(__file__))[0]
except IndexError:
    print("No day in file")
    sys.exit()


def make_rule(i, rules):
    options = rules[i]
    rule_options = []
    for option in options:
        option = option.strip()
        if option[0] == "\"":
            return [option[1:-1]]
        else:
            ruleNums = [x.strip() for x in option.split()]
            sub_options = [make_rule(x, rules) for x in ruleNums]
            new_options = []
            prev_options = [""]
            for option_list in sub_options:
                for option in option_list:
                    for x in prev_options:
                        new_options.append(x + option)
                prev_options = new_options
                new_options = []
            rule_options += prev_options
    return rule_options

def matches(message, options):
    if message in options:
        return True
    return False

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()

    lines = text.split("\n\n")
    rule_lines = lines[0].splitlines()
    messages = lines[1]
    rules = dict()
    for line in rule_lines:
        line = line.split(":")
        rule_num = line[0]
        options = line[1].split("|")
        rules[rule_num] = options

    messages = messages.splitlines()

    rule_options = make_rule("0", rules)
    rule_options = set(rule_options)
    count = 0
    for message in messages:
        if matches(message, rule_options):
            count += 1

    return count
    

def make_rule2(i, rules, d):
    options = rules[i]
    rule_options = []
    for option in options:
        option = option.strip()
        if option[0] == "\"":
            return [option[1:-1]]
        else:
            ruleNums = [x.strip() for x in option.split()]
            sub_options = [make_rule2(x, rules, d) for x in ruleNums]
            new_options = []
            prev_options = [""]
            for option_list in sub_options:
                for option in option_list:
                    for x in prev_options:
                        new_options.append(x + option)
                prev_options = new_options
                new_options = []
            rule_options += prev_options
    d[i] = rule_options
    return rule_options

def matches2(message, options, d):
    if message in options:
        return True
    else:
        for possible in d['42']:
            if possible in message and possible in message.replace(possible, "", 1):
                result = matches2(message.replace(possible, "", 1), options, d)
                if result:
                    return True
                for x in d['42']:
                    for y in d['11']:
                        for z in d['31']:
                            possible = x + y + z
                            if possible in message and possible in message.replace(possible, "", 1):
                                result = matches2(message.replace(possible, "", 1), options, d)
                                if result:
                                    return True
        return False


def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()

    lines = text.split("\n\n")
    rule_lines = lines[0].splitlines()
    messages = lines[1]
    rules = dict()
    for line in rule_lines:
        line = line.split(":")
        rule_num = line[0]
        options = line[1].split("|")
        rules[rule_num] = options

    messages = messages.splitlines()

    maxLength = max(len(x) for x in messages)

    d = dict()
    rule_options = make_rule2("0", rules, d)
    rule_options = set(rule_options)

    # update rule_options
    # 8 can be the same thing, or same + same
    # 11 can be the same thing, or '42' + '11' + '31'
    # nothing else references 11 or 8, so we just add the loops to the set
    eleven = d['11']
    fourty_two = d['42']
    thirty_one = d['31']
    """
    loopVals = fourty_two + eleven
    for x in fourty_two:
        for y in eleven:
            for z in thirty_one:
                loopVals.append(x + y + z)
    """
    print(len(eleven), len(fourty_two), len(thirty_one))
    count = 0
    for message in messages:
        if matches2(message, rule_options, d):
            count += 1

    return count

print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test2.txt"))
print(solve2(f"input/day{day}input.txt"))
