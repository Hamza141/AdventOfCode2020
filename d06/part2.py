from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')

count = 0
current = defaultdict(int)
num = 0

for l in lines:
    l = l.strip()
    if len(l) == 0:
        for k, v in current.items():
            if v == num:
                count += 1
        current = defaultdict(int)
        num = 0
        continue

    for c in l:
        current[c] += 1
    num += 1


for k, v in current.items():
    if v == num:
        count += 1

print(count)
