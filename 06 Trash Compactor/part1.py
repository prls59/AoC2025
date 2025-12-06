import os
from functools import reduce

datafile = "input.txt"

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    rows = input.read()[0:-1].split("\n")

operations = rows.pop().split()

problem_count = len(rows[0].split())
number_count = len(rows)

worksheet = [[0 for y in range(number_count)] for x in range(problem_count)]

for y in range(number_count):
    row = rows[y].split()
    for x in range(problem_count):
        worksheet[x][y] = int(row[x])

grand_total = 0

for x in range(problem_count):
    if operations[x] == '*':
        grand_total += reduce(lambda a, b: a * b, worksheet[x])
    else:
        grand_total += reduce(lambda a, b: a + b, worksheet[x])

print('Result = ', grand_total)