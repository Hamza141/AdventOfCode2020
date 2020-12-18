from collections import deque
import sys
from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d18\\input.txt')

i = 0


def getIndex(s, i):
    # If input is invalid.
    if s[i] != '(':
        return -1

    # Create a deque to use it as a stack.
    d = deque()

    # Traverse through all elements
    # starting from i.
    for k in range(i, len(s)):

        # Pop a starting bracket
        # for every closing bracket
        if s[k] == ')':
            d.popleft()

        # Push all starting brackets
        elif s[k] == '(':
            d.append(s[i])

        # If deque becomes empty
        if not d:
            return k

    return -1


def solve(expression):
    result = 0
    i = 0
    current = ''
    symbol = ''
    while i < len(expression):
        c = expression[i]
        if c == ' ':
            i += 1
            continue
        if c.isnumeric():
            current += c
        elif c == '+' or c == '*':
            if symbol != '':
                if symbol == '+':
                    result += int(current)
                elif symbol == '*':
                    result *= int(current)
            else:
                if current != '':
                    result = int(current)
            symbol = c
            current = ''
        elif c == '(':
            last_index = getIndex(expression, i)
            res, n_i = solve(expression[i+1:last_index])
            if symbol == '+':
                result += int(res)
            elif symbol == '*':
                result *= int(res)
            else:
                result = res
            symbol = ''
            i += n_i + 1

        i += 1
    if current != '':
        if symbol == '+':
            result += int(current)
        elif symbol == '*':
            result *= int(current)
    return (result, i)


result = 0
stack = []
d = {}
index = 0
while i < len(lines):
    l = lines[i].strip()
    res, _ = solve(l)
    result += res

    i += 1

print(result)
