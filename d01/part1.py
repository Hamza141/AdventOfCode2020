def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')
s = set()
for l in lines:
    diff = 2020 - int(l)
    if diff in s:
        print(diff * int(l))
    else:
        s.add(int(l))
