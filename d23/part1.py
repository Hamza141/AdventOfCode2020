import re
from collections import deque
import sys
from copy import copy, deepcopy
from collections import defaultdict
from lark import Lark


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d23\\input.txt')

i = 0
nums = []

while i < len(lines):
    l = lines[i].strip()
    for c in l:
        nums.append(int(c))
    i += 1

print(nums)

min_ = min(nums)
max_ = max(nums)
i = 0
last_value = nums[-1]
while i < 100:
    index = (nums.index(last_value) + 1) % len(nums)
    current = nums[index]
    last_value = current

    j = 0
    pick_up = []
    while j < 3:
        pick_up.append(nums.pop((nums.index(last_value)+1) % len(nums)))
        j += 1

    current -= 1

    dest = None
    while dest == None:
        try:
            dest = nums.index(current) + 1
        except Exception:
            current -= 1
            if current < min_:
                current = max_

    j = 0
    while j < 3:
        nums.insert((dest + j), pick_up[j])
        j += 1
    print(nums)
    i += 1

start = nums.index(1)
i = 0
out = ''
while i < len(nums) - 1:
    start = (start+1) % len(nums)
    out += str(nums[start])
    i += 1

print(out)