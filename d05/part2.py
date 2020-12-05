def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')

highest = 0


def find_col(code):
    high = 7
    low = 0
    current = 0
    mid = 0
    while current < 3:
        mid = (high + low) // 2
        if code[current] == 'L':
            high = mid
            if current == 2:
                return min(low, high)
        elif code[current] == 'R':
            low = mid + 1
            if current == 2:
                return max(low, high)
        current += 1
    return mid


def find_row(code):
    high = 127
    low = 0
    current = 0
    mid = 0
    while current < 7:
        mid = (high + low) // 2
        if code[current] == 'F':
            high = mid
            if current == 6:
                return min(low, high)
        elif code[current] == 'B':
            low = mid + 1
            if current == 6:
                return max(low, high)
        current += 1
    return mid


seats = set()
max_row = 0
for l in lines:
    l = l.strip()
    row = find_row(l[:-3])
    col = find_col(l[-3:])
    seats.add((row * 8) + col)
    if highest < (row * 8) + col:
        highest = (row * 8) + col

for i in range(911):
    if i not in seats:
        print(i)
