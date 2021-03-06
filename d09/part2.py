from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d09\\input.txt')

value = 0
i = 0
seen = []


def two_sum(nums, target):
    required = {}
    for i in range(len(nums)):
        if target - nums[i] in required:
            return [required[target - nums[i]], i]
        else:
            required[nums[i]] = i


invalid = 0
while i < len(lines):
    l = lines[i].strip()
    num = int(l)
    if len(seen) < 25:
        seen.append(num)
    else:
        s = two_sum(seen, num)
        if s is None:
            invalid = num
            break
        else:
            seen.append(num)
            seen = seen[1:]
    i += 1

i = 0
seen = []
while i < len(lines):
    l = lines[i].strip()
    num = int(l)
    if sum(seen) < invalid:
        seen.append(num)
    elif sum(seen) > invalid:
        seen = seen[1:]
        continue
    elif sum(seen) == invalid:
        break
    i += 1

m1 = max(seen)
m2 = min(seen)
print(m1 + m2)
