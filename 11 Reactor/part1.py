import os, time, datetime

start_time = time.time()
datafile = "input.txt"

def dfs(devices, stack, end):
    count = 0
    while stack:
        device = stack.pop()
        if device == end:
            count += 1
        else:
            stack.extend(devices[device])
    return count

devices = {}
start = 'you'
end = 'out'

# Build dictionary of each device and the devices it's connected to.
with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for line in input:
        row = line[0:-1].split(': ')
        devices[row[0]] = row[1].split()

# Depth-first search of paths from 'you' to 'out'
stack = [start]
path_count = dfs(devices, stack, end)

print('Result for', datafile, '=', path_count)
print('Runtime: %s seconds.' % (time.time() - start_time))