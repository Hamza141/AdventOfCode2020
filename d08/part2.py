from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')

def do(trying):
    seen = set()
    value = 0
    i = 0
    while i < len(lines):
        l = lines[i].strip()
        s = l.split(' ')
        if trying == i:
            if s[0] == 'nop':
                s[0] = 'jmp'
            elif s[0] == 'jmp':
                s[0] = 'nop'
            l = ' '.join(s)

        if (i, l) not in seen:
            seen.add((i, l))
        else:
            return False
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
    return True

for j in range(len(lines)):
    if do(j):
        break
    else:
        continue
