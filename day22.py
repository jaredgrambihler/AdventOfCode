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


def win_score(cards_1, cards_2):
    win_cards = cards_1 if cards_1 else cards_2
    val = 0
    for i, card in enumerate(reversed(win_cards)):
        val += (i+1) * card
    return val

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    players = text.split("\n\n")
    cards_1 = [int(x.strip()) for x in players[0].splitlines()[1:]]
    cards_2 = [int(x.strip()) for x in players[1].splitlines()[1:]]

    while (cards_1 and cards_2):
        card_1 = cards_1[0]
        cards_1 = cards_1[1:]
        card_2 = cards_2[0]
        cards_2 = cards_2[1:]
        if card_1 > card_2:
            cards_1 += [card_1, card_2]
        else:
            cards_2 += [card_2, card_1]
    
    return win_score(cards_1, cards_2)
    
def recursive_combat(cards_1, cards_2):
    played = set()
    # while no winner
    while cards_1 and cards_2:
        if (tuple(cards_1), tuple(cards_2)) in played:
            # player 1 wins to avoid infinite recursion
            return cards_1, []
        played.add((tuple(cards_1), tuple(cards_2)))
        card_1 = cards_1[0]
        card_2 = cards_2[0]
        cards_1 = cards_1[1:]
        cards_2 = cards_2[1:]
        if card_1 <= len(cards_1) and card_2 <= len(cards_2):
            result_1, result_2 = recursive_combat(copy.deepcopy(cards_1[:card_1]), copy.deepcopy(cards_2[:card_2]))
            if result_1:
                # player 1 wins
                cards_1 += [card_1, card_2]
            else:
                # player 2 wins
                cards_2 += [card_2, card_1]
        elif card_1 > card_2:
            cards_1 += [card_1, card_2]
        else:
            cards_2 += [card_2, card_1]

    return cards_1, cards_2


def solve2(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    players = text.split("\n\n")
    cards_1 = [int(x.strip()) for x in players[0].splitlines()[1:]]
    cards_2 = [int(x.strip()) for x in players[1].splitlines()[1:]]

    cards_1, cards_2 = recursive_combat(cards_1, cards_2)
    return win_score(cards_1, cards_2)
    
print("Part 1")
print(solve(f"input/day{day}test.txt"))
print(solve(f"input/day{day}input.txt"))

print("Part 2")
print(solve2(f"input/day{day}test.txt"))
print(solve2(f"input/day{day}input.txt"))
