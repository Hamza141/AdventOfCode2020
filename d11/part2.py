from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d11\\input.txt')

chairs = [['' for j in range(len(lines[0].strip()))]
          for i in range(len(lines))]

i = 0
while i < len(lines):
    l = lines[i].strip()
    for j in range(len(l)):
        if l[j] == 'L':
            chairs[i][j] = '#'
        else:
            chairs[i][j] = l[j]
    i += 1

print(chairs)


def check_long(chairs, i, j):
    occupied = 0
    # down
    n_i = i + 1
    while n_i < len(chairs):
        if chairs[n_i][j] == '#':
            occupied += 1
            break
        elif chairs[n_i][j] == 'L':
            break
        n_i += 1
    # up
    n_i = i - 1
    while n_i >= 0:
        if chairs[n_i][j] == '#':
            occupied += 1
            break
        elif chairs[n_i][j] == 'L':
            break
        n_i -= 1
    # right
    n_j = j + 1
    while n_j < len(chairs[0]):
        if chairs[i][n_j] == '#':
            occupied += 1
            break
        elif chairs[i][n_j] == 'L':
            break
        n_j += 1
    # left
    n_j = j - 1
    while n_j >= 0:
        if chairs[i][n_j] == '#':
            occupied += 1
            break
        elif chairs[i][n_j] == 'L':
            break
        n_j -= 1

    # bottom right
    n_i = i + 1
    n_j = j + 1
    while n_i < len(chairs) and n_j < len(chairs[0]):
        if chairs[n_i][n_j] == '#':
            occupied += 1
            break
        elif chairs[n_i][n_j] == 'L':
            break
        n_j += 1
        n_i += 1
    # top right
    n_i = i - 1
    n_j = j + 1
    while n_i >= 0 and n_j < len(chairs[0]):
        if chairs[n_i][n_j] == '#':
            occupied += 1
            break
        elif chairs[n_i][n_j] == 'L':
            break
        n_j += 1
        n_i -= 1

    # top left
    n_i = i - 1
    n_j = j - 1
    while n_i >= 0 and n_j >= 0:
        if chairs[n_i][n_j] == '#':
            occupied += 1
            break
        elif chairs[n_i][n_j] == 'L':
            break
        n_j -= 1
        n_i -= 1
    # bottom left
    n_i = i + 1
    n_j = j - 1
    while n_i < len(chairs) and n_j >= 0:
        if chairs[n_i][n_j] == '#':
            occupied += 1
            break
        elif chairs[n_i][n_j] == 'L':
            break
        n_j -= 1
        n_i += 1
    return occupied


def do(chairs):
    changed = False
    old_chairs = deepcopy(chairs)
    for i in range(len(chairs)):
        for j in range(len(chairs[0])):
            if old_chairs[i][j] == '#':
                if check_long(old_chairs, i, j) >= 5:
                    chairs[i][j] = 'L'
                    changed = True
            elif old_chairs[i][j] == 'L':
                if check_long(old_chairs, i, j) == 0:
                    chairs[i][j] = '#'
                    changed = True
    return changed


i = 1
while True:
    v = do(chairs)
    # print(i)
    # print(chairs)
    if not v:
        break
    i += 1

count = 0
for i in range(len(chairs)):
    for j in range(len(chairs[0])):
        if chairs[i][j] == '#':
            count += 1
print(count)
