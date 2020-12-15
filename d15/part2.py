import sys
from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d15\\input.txt')

i = 0

current = 0
last = 0
seen = defaultdict(list)
nums = []

while i < len(lines):
    l = lines[i].strip()
    l = l.split(',')
    nums = [int(c) for c in l]

    i += 1

i = 0
while i < 30000000:
    if i >= len(nums) and current in seen.keys():
        temp = current
        if len(seen[current]) == 1:
            current = 0
        else:
            current = abs(seen[current][-1] - seen[current][-2])
        last = temp
    else:
        last = current
        current = nums[i % len(nums)]
    seen[current].append(i)
    i += 1

print(current)
