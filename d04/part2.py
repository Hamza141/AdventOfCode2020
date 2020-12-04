import string
import re


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
current = {}

pos_ecl = [
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth',
]


def process():
    global count
    try:
        byr = int(current['byr'])
        if byr < 1920 or byr > 2002 or len(current['byr']) != 4:
            raise ValueError
        iyr = int(current['iyr'])
        if iyr < 2010 or iyr > 2020 or len(current['iyr']) != 4:
            raise ValueError
        eyr = int(current['eyr'])
        if eyr < 2020 or eyr > 2030 or len(current['eyr']) != 4:
            raise ValueError

        hgt = current['hgt']
        hgt_val = int(hgt[:-2])
        measurement = hgt[-2:]
        if 'cm' == measurement:
            if hgt_val < 150 or hgt_val > 193:
                raise ValueError
        elif 'in' == measurement:
            if hgt_val < 59 or hgt_val > 76:
                raise ValueError
        else:
            raise ValueError

        hcl = current['hcl']
        hexes = '0123456789abcdef'
        if hcl[0] != '#':
            raise ValueError
        for c in hcl[1:]:
            if c not in hexes:
                raise ValueError

        ecl = current['ecl']
        if ecl not in pos_ecl or len(ecl) != 3:
            raise ValueError

        pid = current['pid']
        if len(pid) != 9 or not str(pid).isnumeric():
            raise ValueError

        for field in field_list:
            if field not in current:
                raise ValueError

        count += 1
    except Exception:
        pass


for l in lines:
    if len(l) == 1:
        process()
        current = {}
        continue
    pairs = l.strip().split(' ')
    for p in pairs:
        current[p.split(':')[0]] = p.split(':')[1]

process()
print(count)
