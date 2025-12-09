import os

datafile = "input.txt"

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    red_tiles = [[int(x) for x in line.split(',')] for line in input]

largest = 0
for a in range(len(red_tiles) - 1):
    for b in range(a + 1, len(red_tiles)):
        area = (abs(red_tiles[a][0] - red_tiles[b][0]) + 1) * (abs(red_tiles[a][1] - red_tiles[b][1]) + 1)
        if area > largest:
            largest = area

print('Result = ', largest)