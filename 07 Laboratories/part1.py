import os

DATAFILE = "input.txt"

START = 'S'
SPLITTER = '^'

split_count = 0
beams = set()

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    manifold = input.read()[0:-1].split("\n")

length = len(manifold)
width = len(manifold[0])

beams.add(manifold[0].find(START))

for y in range(2, length-1, 2):
    new_beams = set()
    for x in beams:
        if manifold[y][x] == SPLITTER:
            split_count += 1
            if x > 0:
                new_beams.add(x-1)
            if x < width-1:
                new_beams.add(x+1)
        else:
            new_beams.add(x)
    beams = new_beams.copy()

print('Result = ', split_count)