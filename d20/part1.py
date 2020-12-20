import re
from collections import deque
import sys
from copy import copy, deepcopy
from collections import defaultdict
from lark import Lark


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d20\\input.txt')

i = 0
tiles = defaultdict(lambda: defaultdict(list))

while i < len(lines):
    l = lines[i].strip()
    if 'Tile' in l:
        tile_id = l.split('Tile')[1][:-1].strip()
        i += 1
        tile = lines[i:i+10]
        for index, line in enumerate(tile):
            line = line.strip()
            for c in line:
                tiles[tile_id][index].append(c)
        i += 10
        # print(tiles[tile_id])

    i += 1


b_tiles = {}
seen = defaultdict(int)
for tile_id in tiles.keys():
    top = ''
    left = ''
    right = ''
    bottom = ''
    for index in tiles[tile_id]:
        line = tiles[tile_id][index]
        if index == 0:
            top = ''.join(line)
        if index == 9:
            bottom = ''.join(line)
        left += line[0]
        right += line[-1]

    trans = str.maketrans('#.', '10')
    top = top.translate(trans)
    bottom = bottom.translate(trans)
    right = right.translate(trans)
    left = left.translate(trans)
    b_top = int(top, 2)
    b_bottom = int(bottom, 2)
    b_right = int(right, 2)
    b_left = int(left, 2)

    r_top = top[::-1]
    r_bottom = bottom[::-1]
    r_right = right[::-1]
    r_left = left[::-1]
    b_r_top = int(r_top, 2)
    b_r_bottom = int(r_bottom, 2)
    b_r_right = int(r_right, 2)
    b_r_left = int(r_left, 2)

    b_tiles[tile_id] = [[b_top, b_bottom, b_right, b_left],
                        [b_r_top, b_r_bottom, b_r_right, b_r_left]]
    for v in [b_top, b_bottom, b_right, b_left]:
        seen[v] += 1
    for v in [b_r_top, b_r_bottom, b_r_right, b_r_left]:
        seen[v] += 1
    # seen.update([b_top, b_bottom, b_right, b_left])
    # seen.update([b_r_top, b_r_bottom, b_r_right, b_r_left])

    # print(top, bottom, right, left)
    # temp = line.translate(str.maketrans('#.', '10'))
    # print(int(temp, 2))
    # print(temp)

result = 1
min_count = sys.maxsize

for tile_id in b_tiles.keys():
    order_1 = b_tiles[tile_id][0]
    order_2 = b_tiles[tile_id][1]
    count_1 = -1
    count_2 = -1
    for value in order_1:
        count_1 += seen[value]
    for value in order_2:
        if value in seen.keys():
            count_2 += seen[value]
    # print(tile_id)
    # print(count_1, count_2)
    if count_1 < min_count:
        min_count = count_1
        result = int(tile_id)
    elif count_1 == min_count:
        result *= int(tile_id)

print(result)
