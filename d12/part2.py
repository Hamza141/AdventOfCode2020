from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d12\\input.txt')

x = 0
y = 0
w_x = 10
w_y = 1

i = 0


def helper(amount):
    global x
    global y
    x += (w_x * amount)
    y += (w_y * amount)


def helper2(facing, amount):
    global w_x
    global w_y
    if facing == 'N':
        w_y += amount
    if facing == 'S':
        w_y -= amount
    if facing == 'E':
        w_x += amount
    if facing == 'W':
        w_x -= amount


while i < len(lines):
    l = lines[i].strip()
    command = l[0]
    amount = int(l[1:])
    if command == 'F':
        helper(amount)
    elif command == 'L':
        while amount > 0:
            w_x, w_y = -w_y, w_x
            amount -= 90
    elif command == 'R':
        while amount > 0:
            w_x, w_y = w_y, -w_x
            amount -= 90
    else:
        helper2(command, amount)
    i += 1

print(abs(x) + abs(y))
