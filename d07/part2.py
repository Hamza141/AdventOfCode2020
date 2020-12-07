from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')

mapping = defaultdict(list)

for l in lines:
    l = l.strip()
    if 'no other' in l:
        continue
    contain = l.split('contain')
    key = contain[0].split('bags')[0].strip()
    vs = contain[1].split(',')
    values = []
    for v in vs:
        v = v.split('bag')[0].strip().split(' ')
        values.append((v[0], ' '.join(v[1:])))
    mapping[key] = values


def bags(mapping, color):
    count = 1
    for c, col in mapping[color]:
        count += (int(c) * bags(mapping, col))
    return count


print(bags(mapping, 'shiny gold') - 1)
