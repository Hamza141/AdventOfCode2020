def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')
count = 0
i = 0
j = 0
while i < len(lines):
    i += 1
    j += 3
    j = j % len(lines[0].strip())
    print(i, j)
    if i < len(lines) and lines[i][j] == '#':
        print(i, j)
        count += 1
print(count)
