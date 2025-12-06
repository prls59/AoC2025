import os
from functools import reduce

datafile = "input.txt"

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    rows = input.read()[0:-1].split("\n")

operations = rows.pop()

col_count = len(operations)
row_count = len(rows)

grand_total = 0
nums = []
x = col_count - 1

while x >= 0:
    num_str = ''
    for y in range(row_count):
        num_str += rows[y][x]
    nums.append(int(num_str))
    if operations[x] == ' ':
        x -= 1
        continue
    else:
        if operations[x] == '+':
            grand_total += reduce(lambda a, b: a + b, nums)
        else:
            grand_total += reduce(lambda a, b: a * b, nums)
        nums = []
        x -= 2

print('Result = ', grand_total)