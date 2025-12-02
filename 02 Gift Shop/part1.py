import os, math

datafile = "input.txt"

id_ranges = []
invalid_sum = 0


with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    range_strings = input.read()[0:-1].split(",")

for rs in range_strings:
    id_ranges.append([int(x) for x in rs.split('-')])

for id_range in id_ranges:
    #
    # Find smallest number with an even number of digits that's in the range.
    #
    start = id_range[0]
    len = math.floor(math.log10(start)) + 1
    if len % 2 != 0:
        start = 10**len
        len += 1
        if start >= id_range[1]:
            continue
    #
    # Take first half (h) & increment while hh is in range.
    #
    h = int(start // 10**(len/2))
    hh = h + int(h * 10**(len/2))
    while hh <= id_range[1]:
        if hh >= id_range[0]:
            invalid_sum += hh
        h += 1
        hh = h + int(h * 10**(math.floor(math.log10(h)) + 1))

print('Result = ', invalid_sum)