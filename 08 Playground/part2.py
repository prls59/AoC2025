import os

datafile = "input.txt"

box_circuit = {}
distances = {}
circuit_size = {}

NO_CIRCUIT = -1

def distance(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2) ** 0.5

def connect(a, b, circuit_id, circuit_size):
    if box_circuit[a] == NO_CIRCUIT:
        if box_circuit[b] == NO_CIRCUIT:
            box_circuit[a] = circuit_id
            box_circuit[b] = circuit_id
            circuit_size[circuit_id] = 2
            circuit_id += 1
        else:
            box_circuit[a] = box_circuit[b]
            circuit_size[box_circuit[b]] += 1
    else:
        if box_circuit[b] == NO_CIRCUIT:
            box_circuit[b] = box_circuit[a]
            circuit_size[box_circuit[a]] += 1
        else:
            if box_circuit[a] != box_circuit[b]:
                merge_circuits(box_circuit, a, b, circuit_size)
    return circuit_id

def merge_circuits(box_circuit, box1, box2, circuit_size):
    c1 = box_circuit[box1]
    c2 = box_circuit[box2]
    if circuit_size[c1] < circuit_size[c2]:
        from_c = c1
        to_c = c2
    else:
        from_c = c2
        to_c = c1
    change_list = [box for box, circuit in box_circuit.items() if circuit == from_c]
    for box in change_list:
        box_circuit[box] = to_c
    circuit_size[to_c] += circuit_size[from_c]
    circuit_size[from_c] = 0

# Build dictionary of junction box locations, and the circuit they're in (currently none)
with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for line in input:
        row = line[0:-1].split(',')
        box = (int(row[0]), int(row[1]), int(row[2]))
        box_circuit[box] = NO_CIRCUIT

# Build dictionary of distances from a to b (where a < b)
box_list = list(box_circuit)
box_list.sort()
box_count = len(box_list)
for a in range(box_count -1):
    for b in range(a + 1, box_count):
        distances[(box_list[a],box_list[b])] = distance(box_list[a],box_list[b])

# Build list of junction box pairs in distance order
nearby_boxes = sorted(distances, key=lambda k: distances[k])

# create circuits
circuit_id = 0
for c in range(len(nearby_boxes)):
    box1 = nearby_boxes[c][0]
    box2 = nearby_boxes[c][1]
    circuit_id = connect(box1, box2, circuit_id, circuit_size)
    if circuit_size[box_circuit[box1]] == box_count:
        break

# get check product
result = box1[0] * box2[0]

print('Result = ', result)