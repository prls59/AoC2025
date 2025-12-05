import os

datafile = "input.txt"

elf_id_list = []
fresh_ids = []

def add_range(fresh_ids, from_id, to_id):
    range_added = False
    for id_range in fresh_ids:
        if from_id <= id_range[1] and to_id >= id_range[0]:
            id_range[0] = min(id_range[0], from_id)
            id_range[1] = max(id_range[1], to_id)
            range_added = True
            break
    if not range_added:
        fresh_ids.append([from_id, to_id])

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    line = input.readline()[:-1]
    while line != '':
        from_id, to_id = line.split('-')
        elf_id_list.append([int(x) for x in line.split('-')])
        line = input.readline()[0:-1]
    elf_id_list.sort()

    for from_id, to_id in elf_id_list:
        add_range(fresh_ids, from_id, to_id)
        
    fresh_count = 0
    for from_id, to_id in fresh_ids:
        fresh_count += to_id - from_id + 1

print('Result = ', fresh_count)