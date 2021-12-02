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


def make_rule_regex(rules, rule_num):
    if rules[rule_num][0] in ["a", "b"]:
        return rules[rule_num][0]
    else:
        rs = []
        for sub_rule in rules[rule_num]:
            r = ""
            for num in sub_rule.strip().split(" "):
                r += make_rule_regex(rules, num)
            rs.append(r)
        regex = "(" + "|".join(rs) + ")"
        # 8: 42 | 42 8
        # 11: 42 31 | 42 11 31
        # 8 can be a regex of 42 some number of times
        # 11 is 42 31, 42 42 31 31, 42 42 42 31 31 31, ...
        # so some sequence of 42 followed by 31
        # the choice to match it up to 20 times is arbitrary but sufficient
        if rule_num == "8":
            fourty_two = make_rule_regex(rules, "42")
            for i in range(1, 20):
                regex += "|" + "(" + fourty_two  + f"{{{i}}})"
            regex = "(" + regex + ")"
        elif rule_num == "11":
            fourty_two = make_rule_regex(rules, "42")
            thirty_one = make_rule_regex(rules, "31")
            for i in range(1, 20):
                regex += "|" + "(" + fourty_two +f"{{{i}}}" + thirty_one + f"{{{i}}}" + ")"
            regex = "(" + regex + ")"

        return regex

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
        options = line[1].replace("\"", "").strip().split("|")
        rules[rule_num] = options

    messages = messages.splitlines()
    regex = make_rule_regex(rules, "0")

    count = 0
    for message in messages:
        if match := re.match(regex, message):
            if message.replace(match.group(0), "", 1) == "":
                count += 1
    return count

print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test2.txt"))
print(solve2(f"input/day{day}input.txt"))
