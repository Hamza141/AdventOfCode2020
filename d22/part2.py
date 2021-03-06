import re
from collections import deque
import sys
from copy import copy, deepcopy
from collections import defaultdict
from lark import Lark


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d22\\input.txt')

i = 0
player_1 = False
player_2 = False
p1_cards = []
p2_cards = []

while i < len(lines):
    l = lines[i].strip()
    if len(l) == 0:
        i += 1
        continue

    if 'Player 1' in l:
        player_1 = True
        player_2 = False
    elif 'Player 2' in l:
        player_1 = False
        player_2 = True
    else:
        if player_1:
            p1_cards.append(int(l))
        elif player_2:
            p2_cards.append(int(l))

    i += 1

print(p1_cards, p2_cards)

p1_orig = deepcopy(p1_cards)
p2_orig = deepcopy(p2_cards)


seen = set()


def recursive_round(p1_cards, p2_cards):
    seen = set()
    while len(p1_cards) > 0 and len(p2_cards) > 0:
        if ','.join([str(i) for i in p1_cards]) in seen and ','.join([str(i) for i in p2_cards]) in seen:
            return 1

        seen.add(','.join([str(i) for i in p1_cards]))
        seen.add(','.join([str(i) for i in p2_cards]))

        p1 = p1_cards.pop(0)
        p2 = p2_cards.pop(0)

        if len(p1_cards) >= p1 and len(p2_cards) >= p2:
            result = recursive_round(
                deepcopy(p1_cards[:p1]), deepcopy(p2_cards[:p2]))
            if result == 1:
                p1_cards.append(p1)
                p1_cards.append(p2)
            else:
                p2_cards.append(p2)
                p2_cards.append(p1)
            continue

        if p1 > p2:
            p1_cards.append(p1)
            p1_cards.append(p2)
        else:
            p2_cards.append(p2)
            p2_cards.append(p1)

    if len(p1_cards) == 0:
        return 2
    if len(p2_cards) == 0:
        return 1


while len(p1_cards) > 0 and len(p2_cards) > 0:
    p1 = p1_cards.pop(0)
    p2 = p2_cards.pop(0)

    if len(p1_cards) >= p1 and len(p2_cards) >= p2:
        result = recursive_round(
            deepcopy(p1_cards[:p1]), deepcopy(p2_cards[:p2]))
        if result == 1:
            p1_cards.append(p1)
            p1_cards.append(p2)
        else:
            p2_cards.append(p2)
            p2_cards.append(p1)
        continue

    if p1 > p2:
        p1_cards.append(p1)
        p1_cards.append(p2)
    else:
        p2_cards.append(p2)
        p2_cards.append(p1)

print(p1_cards, p2_cards)

score = 0
i = 0

while i < len(p1_cards):
    score += ((i + 1) * p1_cards[len(p1_cards) - 1 - i])
    i += 1

if score == 0:
    while i < len(p2_cards):
        score += ((i + 1) * p2_cards[len(p2_cards) - 1 - i])
        i += 1

print(score)
