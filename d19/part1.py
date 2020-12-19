import re
from collections import deque
import sys
from copy import copy, deepcopy
from collections import defaultdict
from lark import Lark


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d19\\input.txt')

i = 0
rules = ''
inputs = set()

while i < len(lines):
    l = lines[i].strip()

    if ':' in l:
        rules += l + '\n'
    elif len(l) > 0:
        inputs.add(l)

    i += 1

rules = re.sub(r'\b0\b', 'start', rules)

before = 0
after = ord('a')
for i in range(26):
    rules = rules.replace(str(before), chr(after))
    before += 1
    after += 1

l = Lark(f'''
    {rules}
    %import common.WORD   // imports from terminal library
    %ignore " "           // Disregard spaces in text
    '''
         )

match = 0
for i in inputs:
    try:
        l.parse(i)
        match += 1
    except Exception:
        pass

print(match)
