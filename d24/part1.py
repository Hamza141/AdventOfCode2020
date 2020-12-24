import re
from collections import deque
import sys
from copy import copy, deepcopy
from collections import defaultdict
from lark import Lark


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d24\\input.txt')

i = 0

tiles = defaultdict(str)

while i < len(lines):
    l = lines[i].strip()
    j = 0
    x = 0
    y = 0
    z = 0
    while j < len(l):
        direction = l[j]
        if direction == 's' or direction == 'n':
            j += 1
            direction += l[j]
        if direction == 'e':
            x += 1
            z -= 1
        elif direction == 'w':
            x -= 1
            z += 1
        elif direction == 'ne':
            y += 1
            z -= 1
        elif direction == 'nw':
            x -= 1
            y += 1
        elif direction == 'sw':
            y -= 1
            z += 1
        elif direction == 'se':
            x += 1
            y -= 1

        j += 1
    coord = (x, y, z)
    color = tiles[coord]
    if color == '' or color == 'w':
        tiles[coord] = 'b'
    elif color == 'b':
        tiles[coord] = 'w'

    i += 1

out = list(tiles.values()).count('b')
print(out)