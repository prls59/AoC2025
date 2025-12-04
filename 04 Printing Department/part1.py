import os

DATAFILE = "input.txt"

ROLL = '@'
NEIGHBOUR_LIMIT = 3

def neighbour_count(grid_x,grid_y):
    n = 0
    for dy in range(-1,2):
        y = grid_y + dy
        if y < 0 or y >= grid_length:
            continue
        for dx in range (-1,2):
            x = grid_x + dx
            if x < 0 or x >= grid_width or (dx == 0 and dy == 0):
                continue
            if grid[y][x] == ROLL:
                n += 1
    return n

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    rows = input.read()[0:-1].split("\n")

grid_length = len(rows)
grid_width = len(rows[0])

grid = []
for y in range(grid_length):
    grid.append([rows[y][x] for x in range(grid_width)])

accessible_count = 0

for y in range(grid_length):
    for x in range(grid_width):
        if grid[y][x] == ROLL and neighbour_count(x,y) <= NEIGHBOUR_LIMIT:
            accessible_count += 1

print('Result = ', accessible_count)