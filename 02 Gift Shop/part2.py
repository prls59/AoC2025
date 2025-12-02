import os, math
#
# Needed hints for this one :(
#
datafile = "input.txt"

id_ranges = []
invalid_sum = 0

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    range_strings = input.read()[0:-1].split(",")

for rs in range_strings:
    id_ranges.append([int(x) for x in rs.split('-')])
#
# A brute force solution:
#
for s, e in id_ranges:
    #
    # Check every id...
    #
    for id in range(s, e + 1):
        #
        # Convert to string and count non-overlapping repetitions...
        #
        id_string = str(id)
        id_len = len(id_string)
        for n in range(0, id_len // 2):
            if id_string.count(id_string[:n+1]) == id_len / (n + 1):
                invalid_sum += id
                break

print('Result = ', invalid_sum)