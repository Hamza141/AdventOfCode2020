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

    if 'your ticket' in l:
        your_ticket_next = True
    if 'nearby tickets' in l:
        nearby_tickets_next = True

    if not your_ticket_next and not nearby_tickets_next and ':' in l:
        temp = l.index(':')
        field = l[:temp]
        ranges = l[temp+1:].split(' or ')
        criteria[field] = [r.strip() for r in ranges]

    i += 1

error = 0

actual_tickets = []

for ticket in nearby_tickets:
    ticket = ticket.split(',')
    found_count = 0
    for index, value in enumerate(ticket):
        found = False
        value = int(value)
        for k, vs in criteria.items():
            for v in vs:
                v = v.split('-')
                a = int(v[0])
                b = int(v[1])
                if value >= a and value <= b:
                    found = True
                    found_count += 1
                    break
            if found:
                break
    if found_count == len(ticket):
        actual_tickets.append(ticket)


actual_tickets.append(your_ticket.split(','))

possible_mapping = defaultdict(set)
for i in range(len(your_ticket.split(','))):
    possible_mapping[i] = set(criteria.keys())

for ticket in actual_tickets:
    ticket_mapping = defaultdict(set)
    for index, value in enumerate(ticket):
        value = int(value)
        for field, vs in criteria.items():
            found = False
            for v in vs:
                v = v.split('-')
                a = int(v[0])
                b = int(v[1])
                if value >= a and value <= b:
                    found = True
                    break
            if found:
                ticket_mapping[index].add(field)
        possible_mapping[index] = possible_mapping[index].intersection(
            ticket_mapping[index])


final_mapping = {}
i = 0
while True:
    for key, fields in possible_mapping.items():
        if len(fields) == 1:
            field = list(fields)[0]
            for k, f in possible_mapping.items():
                if k != key and field in f:
                    possible_mapping[k].remove(field)
    done = True
    for key, fields in possible_mapping.items():
        if len(fields) != 1:
            done = False
            break
    if done:
        break

result = 1
your_ticket = your_ticket.split(',')
for key, field in possible_mapping.items():
    if 'departure' in list(field)[0]:
        result *= int(your_ticket[key])
print(result)
