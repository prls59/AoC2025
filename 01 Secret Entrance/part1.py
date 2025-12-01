import os

datafile = "input.txt"

dialsize = 100
pos = 50
zeroes = 0

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for line in input:
        dir = 1 if line[0] == "R" else -1
        rot = int(line[1:-1]) * dir
        pos = (pos + rot) % dialsize
        if pos == 0:
            zeroes += 1

print('Result = ', zeroes)