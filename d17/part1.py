import sys
from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d17\\input.txt')

i = 0
state = defaultdict(lambda: defaultdict(list))

while i < len(lines):
    l = lines[i].strip()
    for index, c in enumerate(l):
        state[0][i].append(c)
    i += 1

print(state)


def check_neigh(state, x, y, z):
    count = 0
    value = '.'
    try:
        value = state[z][x][y]
    except IndexError:
        pass

    try:
        if state[z+1][x][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z+1][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z+1][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z+1][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z+1][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z+1][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z+1][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z+1][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z+1][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z-1][x][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z-1][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z-1][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z-1][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z-1][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z-1][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z-1][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z-1][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z-1][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z][x+1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z][x-1][y] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z][x][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z][x][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z][x+1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z][x-1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z][x+1][y-1] == '#':
            count += 1
    except IndexError:
        pass

    try:
        if state[z][x-1][y+1] == '#':
            count += 1
    except IndexError:
        pass

    if value == '#' and (count == 2 or count == 3):
        return '#'
    if value == '.' and (count == 3):
        return '#'
    return '.'


def pad(state):
    max_x = len(state[0])
    max_y = len(state[0][0])
    new_state = defaultdict(lambda: defaultdict(list))
    for k in state.keys():
        i = 0
        while i < max_x:
            if i == 0:
                j = 0
                while j < max_y + 2:
                    new_state[k][i].append('.')
                    j += 1
            j = 0
            while j < max_y:
                if j == 0:
                    new_state[k][i+1].append('.')

                new_state[k][i+1].append(state[k][i][j])

                if j == max_y - 1:
                    new_state[k][i+1].append('.')
                j += 1
            if i == max_x - 1:
                j = 0
                while j < max_y + 2:
                    new_state[k][i+2].append('.')
                    j += 1
            i += 1
    return new_state


def do(state):
    state = pad(state)
    min_z = min(state.keys()) - 1
    max_z = max(state.keys()) + 1

    max_x = len(state[0])
    max_y = len(state[0][0])

    k = min_z
    new_state = defaultdict(lambda: defaultdict(list))
    while k <= max_z:
        i = 0
        while i < max_x:
            j = 0
            while j < max_y:
                val = check_neigh(state, i, j, k)
                new_state[k][i].append(val)
                j += 1

            i += 1

        k += 1
    return new_state


for i in range(6):
    if i == 2:
        a = 2
    state = do(state)

count = 0
for k in state.keys():
    for i in range(len(state[k])):
        for j in range(len(state[k][i])):
            if state[k][i][j] == '#':
                count += 1
print(count)
