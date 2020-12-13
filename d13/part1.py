import sys
from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d13\\input.txt')

i = 0
time = 0
buses = []
earliest = sys.maxsize
e_id = 0

while i < len(lines):
    l = lines[i].strip()
    if i == 0:
        time = int(l)
    else:
        buses = l.split(',')
        for b in buses:
            if b != 'x':
                b = int(b)
                b_time = ((time // b) + 1) * b
                if b_time < earliest:
                    earliest = b_time
                    e_id = b

    i += 1
print(earliest)
print((earliest - time) * e_id)
