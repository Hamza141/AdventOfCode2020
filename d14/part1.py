import sys
from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d14\\input.txt')

i = 0
mask = 0
memory = {}

while i < len(lines):
    l = lines[i].strip()
    if 'mask' in l:
        l = l.split()[2].strip()
        mask = l
    else:
        index = l.split('] =')[0][4:].strip()
        value = l.split('] =')[1].strip()
        b_value = bin(int(value))[2:]
        result = ''
        for j, b in enumerate(mask):
            if b == 'X':
                k = len(mask) - j
                if k <= len(b_value):
                    result += b_value[len(b_value) - k]
                elif result != '':
                    result += '0'
            else:
                result += b
        memory[index] = int(result, 2)

    i += 1

print(sum(memory.values()))