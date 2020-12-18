from collections import deque
import sys
from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d18\\input.txt')

i = 0


# src: https://www.geeksforgeeks.org/find-index-closing-bracket-given-opening-bracket-expression/
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
    i = 0
    current = ''
    stack = []
    while i < len(expression):
        c = expression[i]
        if c == ' ':
            i += 1
            continue
        if c.isnumeric():
            current += c
        elif c == '+' or c == '*':
            stack.append(current)
            stack.append(c)
            current = ''
        elif c == '(':
            last_index = getIndex(expression, i)
            res, n_i = solve(expression[i+1:last_index])
            stack.append(res)
            i += n_i + 1

        i += 1
    stack.append(current)
    return (new_solve(stack), i)


def new_solve(stack):
    new_stack = []
    i = 0
    while i < len(stack):
        value = stack[i]
        if value == '':
            i += 1
            continue
        if str(value).isnumeric():
            new_stack.append(value)
        elif value == '+':
            new_stack.append(int(new_stack.pop()) + int(stack[i+1]))
            i += 1
        i += 1

    result = 1
    for n in new_stack:
        result *= int(n)
    return result


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
