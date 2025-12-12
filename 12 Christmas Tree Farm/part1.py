import os, time, datetime

# Didn't know how to approach this in a way that would run in a reasonable amount of time.
# Saw a hint that the input is very benign, so decided to code a very simple test...

start_time = time.time()
print('Started:', datetime.datetime.now().time())

datafile = "input.txt"
shapes = []
volumes = []
regions = []
fit_count = 0

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    line = input.readline()[:-1]
    while line != '':
        if len(line) == 2:
            vol = 0
            shape = []
            line = input.readline()[:-1]
            while line != '':
                shape.append(line)
                vol += line.count('#')
                line = input.readline()[:-1]
            shapes.append(shape)
            volumes.append(vol)
            line = input.readline()[:-1]

        else:
            size = [int(x) for x in line.split(':')[0].split('x')]
            quantities = [int(x) for x in line.split(':')[1].split()]
            regions.append([size,quantities])
            line = input.readline()[0:-1]

for region in regions:
    width = region[0][0]
    length = region[0][1]
    tot_vol = 0
    for n in range(len(region[1])):
        tot_vol += region[1][n] * volumes[n]
    if tot_vol <= width * length:
        fit_count += 1

print('Finished:', datetime.datetime.now().time())
print('Runtime: %s seconds.' % (time.time() - start_time))
print('   *** Result for', datafile, '=', fit_count, '***')