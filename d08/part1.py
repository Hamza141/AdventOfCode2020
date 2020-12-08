from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')

value = 0
i = 0
seen = set()

while i < len(lines):
    l = lines[i].strip()
    if (i, l) not in seen:
        seen.add((i, l))
    else:
        break
    if 'nop' in l:
        i += 1
        continue
    s = l.split(' ')
    if s[0] == 'acc':
        if s[1][0] == '+':
            value += int(s[1][1:])
        else:
            value -= int(s[1][1:])
        i += 1
    elif s[0] == 'jmp':
        if s[1][0] == '+':
            i += int(s[1][1:])
        else:
            i -= int(s[1][1:])

print(value)
