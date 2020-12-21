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
all_ingre = set()
while i < len(lines):
    l = lines[i].strip()
    l = l.split('contains')
    ingre = l[0][:-2].split()
    aller = l[1].strip()[:-1].split(', ')
    for ing in ingre:
        all_ingre.add(ing)

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


taken = set()
for k in mapping.keys():
    mapping[k] = mapping[k] - safe_ingre
    if len(mapping[k]) == 1:
        taken.add(list(mapping[k])[0])

while True:
    count = 0
    for k in mapping.keys():
        if len(mapping[k]) == 1:
            taken.add(list(mapping[k])[0])
            count += 1
            continue
        before = len(mapping[k])
        mapping[k] -= taken
        if len(mapping[k]) == 1:
            taken.add(list(mapping[k])[0])
        after = len(mapping[k])
        if before == after and len(mapping[k]) == 1:
            count += 1

    if count == len(mapping):
        break
print(mapping)


out = ''
for k in sorted(mapping.keys()):
    out += list(mapping[k])[0]+','
print(out[:-1])
