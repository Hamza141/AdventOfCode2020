import sys
from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d17\\input.txt')

i = 0
state = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

while i < len(lines):
    l = lines[i].strip()
    for index, c in enumerate(l):
        state[0][0][i].append(c)
    i += 1

print(state)


def count_all(state):
    count = 0
    for l in state.keys():
        for k in state[0].keys():
            for i in range(len(state[l][k])):
                for j in range(len(state[l][k][i])):
                    if state[l][k][i][j] == '#':
                        count += 1
    return count


def check_neigh(state, x, y, z, w):
    count = 0
    value = '.'
    try:
        value = state[w][z][x][y]
    except IndexError:
        pass

    try:
        if state[w][z+1][x][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z+1][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z+1][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z+1][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z+1][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z+1][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z+1][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z+1][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z+1][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z-1][x][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z-1][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z-1][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z-1][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z-1][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z-1][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z-1][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z-1][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z-1][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w][z][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z+1][x][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z+1][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z+1][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z+1][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z+1][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z+1][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z+1][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z+1][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z+1][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z-1][x][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z-1][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z-1][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z-1][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z-1][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z-1][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z-1][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z-1][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z-1][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z+1][x][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z+1][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z+1][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z+1][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z+1][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z+1][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z+1][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z+1][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z+1][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z-1][x][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z-1][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z-1][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z-1][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z-1][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z-1][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z-1][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z-1][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z-1][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w-1][z][x][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[w+1][z][x][y] == '#':
            count += 1
    except IndexError:
        pass

    if value == '#' and (count == 2 or count == 3):
        return '#'
    if value == '.' and (count == 3):
        return '#'
    return '.'


def pad(state):
    max_x = len(state[0][0])
    max_y = len(state[0][0][0])
    new_state = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for l in state.keys():
        for k in state[0].keys():
            i = 0
            while i < max_x:
                if i == 0:
                    j = 0
                    while j < max_y + 2:
                        new_state[l][k][i].append('.')
                        j += 1
                j = 0
                while j < max_y:
                    if j == 0:
                        new_state[l][k][i+1].append('.')

                    new_state[l][k][i+1].append(state[l][k][i][j])

                    if j == max_y - 1:
                        new_state[l][k][i+1].append('.')
                    j += 1
                if i == max_x - 1:
                    j = 0
                    while j < max_y + 2:
                        new_state[l][k][i+2].append('.')
                        j += 1
                i += 1
    return new_state


def do(state):
    state = pad(state)
    min_z = min(state.keys()) - 1
    max_z = max(state.keys()) + 1

    max_x = len(state[0][0])
    max_y = len(state[0][0][0])

    new_state = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    l = min_z
    while l <= max_z:
        k = min_z
        while k <= max_z:
            i = 0
            while i < max_x:
                j = 0
                while j < max_y:
                    val = check_neigh(state, i, j, k, l)
                    new_state[l][k][i].append(val)
                    j += 1

                i += 1

            k += 1
        l += 1
    return new_state


for i in range(6):
    if i == 1:
        a = 2
    state = do(state)


print(count_all(state))
