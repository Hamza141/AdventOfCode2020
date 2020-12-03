def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        for k in range(j+1, len(lines)):
            if int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020:
                print(int(lines[i]) * int(lines[j]) * int(lines[k]))
