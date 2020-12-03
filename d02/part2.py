def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')
correct = 0
for l in lines:
    l = l.split(' ')
    minimum = int(l[0].split('-')[0])
    maximum = int(l[0].split('-')[1])
    char = l[1][0]
    password = l[2]
    if bool(password[minimum - 1] == char) ^ bool(password[maximum - 1] == char):
        print(l)
        correct += 1
print(correct)
