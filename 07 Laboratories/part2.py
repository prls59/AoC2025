import os

DATAFILE = "input.txt"

START = 'S'
SPLITTER = '^'
SPACE = '.'

beams = {}

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    manifold = input.read()[0:-1].split("\n")

length = len(manifold)
width = len(manifold[0])

beams[manifold[0].find(START)] = 1

for y in range(2, length-1, 2):
    new_beams = {}
    for x in beams.keys():
        if manifold[y][x] == SPLITTER:
            if x > 0:
                new_beams[x-1] = new_beams.get(x-1,0) + beams[x]
            if x < width-1:
                new_beams[x+1] = new_beams.get(x+1,0) + beams[x]
        else:
            new_beams[x] = new_beams.get(x,0) + beams[x]
    beams = new_beams.copy()

print('Result = ', sum(beams.values()))