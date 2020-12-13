import sys
from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d13\\input.txt')

i = 0
time = 0
buses = []

while i < len(lines):
    l = lines[i].strip()
    if i == 0:
        time = int(l)
    else:
        buses = l.split(',')

    i += 1

minVal = 0
runningProd = 1
for i, num in enumerate(buses):
    if num == 'x':
        continue
    while (minVal + i) % int(num) != 0:
        minVal += runningProd
    runningProd *= int(num)

print(minVal)

