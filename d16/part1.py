import sys
from copy import copy, deepcopy
from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2020\\d16\\input.txt')

i = 0
your_ticket = ''
your_ticket_next = False
nearby_tickets = []
nearby_tickets_next = False
criteria = defaultdict(list)

while i < len(lines):
    l = lines[i].strip()
    if l == '':
        i += 1
        continue

    if your_ticket_next:
        your_ticket = l
        your_ticket_next = False
    if nearby_tickets_next:
        nearby_tickets.append(l)
        # nearby_tickets_next = False

    if 'your ticket' in l:
        your_ticket_next = True
    if 'nearby tickets' in l:
        nearby_tickets_next = True

    if not your_ticket_next and not nearby_tickets_next and ':' in l:
        temp = l.index(':')
        field = l[:temp]
        ranges = l[temp+1:].split(' or ')
        # for r in ranges:
        criteria[field] = [r.strip() for r in ranges]

    i += 1

print(criteria)
print(nearby_tickets)

error = 0

for ticket in nearby_tickets:
    ticket = ticket.split(',')
    for index, value in enumerate(ticket):
        value = int(value)
        found = False
        for k, vs in criteria.items():
            for v in vs:
                v = v.split('-')
                a = int(v[0])
                b = int(v[1])
                if value >= a and value <= b:
                    found = True
                    break
        if not found:
            error += value

print(error)