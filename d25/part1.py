import re
from collections import deque
import sys
from copy import copy, deepcopy
from collections import defaultdict
from lark import Lark


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d25\\input.txt')


def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value = value % 20201227
    return value


def find_loop_size(pub_key):
    loop_size = 0
    value = 1
    while value != pub_key:
        loop_size += 1
        value *= 7
        value = value % 20201227
    return loop_size


card_pub_key = int(lines[0].strip())
card_loop_size = find_loop_size(card_pub_key)
print(card_loop_size)

door_pub_key = int(lines[1].strip())
door_loop_size = find_loop_size(door_pub_key)
print(door_loop_size)

print(transform(door_pub_key, card_loop_size))
