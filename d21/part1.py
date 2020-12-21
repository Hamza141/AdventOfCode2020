import re
from collections import deque
import sys
from copy import copy, deepcopy
from collections import defaultdict
from lark import Lark


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d21\\input.txt')

i = 0
mapping = defaultdict(set)
ing_counts = defaultdict(int)
all_ingre = set()
while i < len(lines):
    l = lines[i].strip()
    l = l.split('contains')
    ingre = l[0][:-2].split()
    aller = l[1].strip()[:-1].split(', ')
    for ing in ingre:
        all_ingre.add(ing)
        ing_counts[ing] += 1

    for a in aller:
        if a in mapping.keys():
            mapping[a] = mapping[a].intersection(set(ingre))
        else:
            mapping[a] = set(ingre)

    i += 1

possible = set()
for vs in mapping.values():
    for v in vs:
        possible.add(v)
safe_ingre = all_ingre - possible

out = 0
for ing in safe_ingre:
    out += ing_counts[ing]
print(out)
