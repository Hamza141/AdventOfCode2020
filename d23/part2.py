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
nums = {}
nums_list = []

while i < len(lines):
    l = lines[i].strip()
    for index, c in enumerate(l):
        nums_list.append(int(c))
    i += 1

i = 1
while i < len(nums_list):
    nums[nums_list[i - 1]] = nums_list[i]
    i += 1

nums[nums_list[-1]] = max(nums_list) + 1
i = max(nums_list) + 1
while len(nums) != 1000000:
    nums[i] = i + 1
    i += 1
nums[max(nums.keys())] = nums_list[0]


min_ = min(nums.keys())
max_ = max(nums.keys())
i = 0
last_value = max_

while i < 10000000:
    current = nums[last_value]

    last_value = current

    j = 0
    pick_up = []
    while j < 3:
        pick_up.append(nums[current])
        current = nums[current]
        j += 1

    current = last_value
    nums[current] = nums[pick_up[-1]]

    for j in pick_up:
        nums.pop(j)

    current -= 1

    temp = None
    while temp == None:
        try:
            temp = nums[current]
        except Exception:
            current -= 1
            if current < min_:
                current = max_

    for j in pick_up:
        nums[current] = j
        current = j
    nums[pick_up[-1]] = temp

    i += 1

print(nums[1])
print(nums[nums[1]])
print(nums[1] * nums[nums[1]])
