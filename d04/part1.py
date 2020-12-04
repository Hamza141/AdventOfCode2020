def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


field_list = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

opt = 'cid'

lines = readFile('input.txt')
count = 0
temp_list = []
field_list.sort()
current = []
for l in lines:
    if len(l) == 1:
        if 'cid' in current:
            current.remove('cid')
        current.sort()
        if current == field_list:
            count += 1
        current = []
        continue
    pairs = l.strip().split(' ')
    fields = []
    for p in pairs:
        fields.append(p.split(':')[0])
    current += fields

print(count)
