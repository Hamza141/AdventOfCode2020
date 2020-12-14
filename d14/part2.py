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


def all_possible(result):
    current = ['']
    for i, r in enumerate(result):
        if r == 'X':
            recurse = all_possible(result[i+1:])
            z = ['0' + c for c in recurse]
            o = ['1' + c for c in recurse]
            new = []
            for c in current:
                for d in z:
                    new.append(c + d)
                for d in o:
                    new.append(c + d)
            return new
        else:
            current = [c + r for c in current]
    return current


while i < len(lines):
    l = lines[i].strip()
    if 'mask' in l:
        l = l.split()[2].strip()
        mask = l
    else:
        index = l.split('] =')[0][4:].strip()
        value = l.split('] =')[1].strip()
        b_index = bin(int(index))[2:]
        result = ''
        for j, b in enumerate(mask):
            if b != 'X':
                if b == '1':
                    result += '1'
                else:
                    k = len(mask) - j
                    if k <= len(b_index):
                        result += b_index[len(b_index) - k]
                    else:
                        result += '0'
            else:
                result += b
        current = ''
        indexes = set(all_possible(result))
        for a in indexes:
            memory[int(a, 2)] = int(value)

    i += 1

print(sum(memory.values()))
