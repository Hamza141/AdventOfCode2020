from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d12\\input.txt')

x = 0
y = 0
heading = 'E'

i = 0

cycle = ['N', 'E', 'S', 'W']


def helper(facing, amount):
    global x
    global y
    if facing == 'N':
        y += amount
    if facing == 'S':
        y -= amount
    if facing == 'E':
        x += amount
    if facing == 'W':
        x -= amount


while i < len(lines):
    l = lines[i].strip()
    command = l[0]
    amount = int(l[1:])
    if command == 'F':
        helper(heading, amount)
    elif command == 'L':
        current = cycle.index(heading)
        while amount > 0:
            current = (current - 1) % 4
            heading = cycle[current]
            amount -= 90
    elif command == 'R':
        current = cycle.index(heading)
        while amount > 0:
            current = (current + 1) % 4
            heading = cycle[current]
            amount -= 90
    else:
        helper(command, amount)

    i += 1

print(abs(x) + abs(y))

