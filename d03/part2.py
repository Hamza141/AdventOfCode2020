def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')
ii = [1, 1, 1, 1, 2]
jj = [1, 3, 5, 7, 1]
answer = 1
for k in range(len(ii)):
    count = 0
    i = 0
    j = 0
    while i < len(lines):
        i += ii[k]
        j += jj[k]
        j = j % len(lines[0].strip())
        if i < len(lines) and lines[i][j] == '#':
            count += 1
    answer *= count
print(answer)