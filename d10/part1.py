from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d10\\input.txt')

value = 0
i = 0
diffs = defaultdict(int)
seen = []


while i < len(lines):
    l = lines[i].strip()
    l = int(l)
    seen.append(l)
    i += 1

seen.sort()

current = 0
c_i = 0
prev = 0
i = 0
while i < len(seen):
    n = seen[i]
    diff = n - current
    diffs[diff] += 1
    i += 1
    current = seen[c_i]
    c_i += 1

print(diffs)
print(diffs[1] * (diffs[3] + 1))
