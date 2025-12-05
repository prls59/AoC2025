import os

datafile = "input.txt"

fresh_ids = []

def check_fresh(fresh_ids, id):
    fresh = False
    for id_range in fresh_ids:
        if id >= id_range[0] and id <= id_range[1]:
            fresh = True
            break
    return fresh

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    line = input.readline()[:-1]
    while line != '':
        from_id, to_id = line.split('-')
        fresh_ids.append([int(x) for x in line.split('-')])
        line = input.readline()[0:-1]

    fresh_count = 0
    id = input.readline()[0:-1]
    while id != '':
        if check_fresh(fresh_ids, int(id)):
            fresh_count += 1
        id = input.readline()[0:-1]
        
print('Result = ', fresh_count)