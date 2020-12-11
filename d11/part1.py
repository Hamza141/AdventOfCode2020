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


def check_adjacent(chairs, i, j):
    occupied = 0
    if i+1 < len(chairs) and chairs[i + 1][j] == '#':
        occupied += 1
    if i-1 >= 0 and chairs[i - 1][j] == '#':
        occupied += 1
    if j+1 < len(chairs[0]) and chairs[i][j+1] == '#':
        occupied += 1
    if j-1 >= 0 and chairs[i][j - 1] == '#':
        occupied += 1
    if i+1 < len(chairs) and j+1 < len(chairs[0]) and chairs[i + 1][j + 1] == '#':
        occupied += 1
    if i-1 >= 0 and j-1 >= 0 and chairs[i - 1][j - 1] == '#':
        occupied += 1
    if i+1 < len(chairs) and j-1 >= 0 and chairs[i + 1][j - 1] == '#':
        occupied += 1
    if i-1 >= 0 and j+1 < len(chairs[0]) and chairs[i - 1][j + 1] == '#':
        occupied += 1

    return occupied


def do(chairs):
    changed = False
    old_chairs = deepcopy(chairs)
    for i in range(len(chairs)):
        for j in range(len(chairs[0])):
            if old_chairs[i][j] == '#':
                if check_adjacent(old_chairs, i, j) >= 4:
                    chairs[i][j] = 'L'
                    changed = True
            elif old_chairs[i][j] == 'L':
                if check_adjacent(old_chairs, i, j) == 0:
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
