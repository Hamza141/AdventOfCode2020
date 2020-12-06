def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')

count = 0
current = set()

for l in lines:
    l = l.strip()
    if len(l) == 0:
        count += len(current)
        current = set()
        continue

    for c in l:
        current.add(c)


count += len(current)

print(count)
