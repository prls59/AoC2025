#
# A neat solution from Reddit for future reference
#

import os, time, datetime

from functools import cache, reduce
from itertools import permutations
from operator import mul

start_time = time.time()
datafile = "input.txt"

G: dict[str, set[str]] = dict()

for line in open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile):
    G[line.split(':')[0]] = set(map(str.strip, line[:-1].split(':')[1].split()))

@cache
def visit(curr: str, dest: str):
    if curr == dest: return 1
    return sum(visit(n, dest) for n in G.get(curr, set()))

s = 0
for r in [['svr'] + list(p) + ['out'] for p in permutations(['fft', 'dac'])]:
    s += reduce(mul, (visit(r[i], r[i+1]) for i in range(len(r)-1)))

print(s)