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


def pop_edges(tiles):
    copy_tiles = deepcopy(tiles)
    for k, v in tiles.items():
        x1, y1, z1 = k
        directions = ['e', 'se', 'sw', 'w', 'nw', 'ne']
        if v == 'w':
            continue
        for direction in directions:
            x = x1
            y = y1
            z = z1
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
            coord = (x, y, z)
            color = ''
            if coord in tiles:
                color = tiles[coord]
            if color == '' or color == 'w':
                copy_tiles[coord] = 'w'
    return copy_tiles


def do(tiles):
    tiles = pop_edges(tiles)
    copy_tiles = deepcopy(tiles)
    for k, v in tiles.items():
        x1, y1, z1 = k
        directions = ['e', 'se', 'sw', 'w', 'nw', 'ne']
        c_b = 0
        for direction in directions:
            x = x1
            y = y1
            z = z1
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
            coord = (x, y, z)
            color = ''
            if coord in tiles:
                color = tiles[coord]
            if color == 'b':
                c_b += 1
        if c_b == 0:
            copy_tiles.pop(k)
            continue
        color = v
        if color == 'b' and (c_b == 0 or c_b > 2):
            copy_tiles[k] = 'w'
        elif color == 'w' and c_b == 2:
            copy_tiles[k] = 'b'
    return copy_tiles


i = 0
out = 0
while i < 100:
    tiles = do(tiles)
    i += 1
out = list(tiles.values()).count('b')
print(out)
