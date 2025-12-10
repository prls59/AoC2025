import os, time, datetime, scipy

datafile = "input.txt"

#
# Tried naive approach, adapting part1 code, much too slow....
# Needed hint to treat as an integral linear programming problem.
# Decided to use SciPy...
#

total_presses = 0
start_time = time.time()
line_count = 0

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for line in input:
        line_count += 1
        print('Processing line:', line_count, datetime.datetime.now().time())
        row = line[0:-1].split()
        # Store target joltage levels
        target = [int(x) for x in row[-1][1:-1].split(',')]
        # Store buttons
        buttons = []
        for button_str in row[1:-1]:
            button = [int(x) for x in button_str[1:-1].split(',')]
            buttons.append(button)

#
# The SciPy bit.
# c: a list of coefficients: all '1's as each counter only increments by 1.
#    Coincidentally this doubles as the integrality parameter, where 1 => integer. In other words,
#    each button must be pressed an integral number of times.
# A: a list of which buttons affect each counter. I think this should comprise '1's for each
#    counter incremented by a button, but the example here uses True equivalently.
# constraints: combines A with the upper and lower bounds of each counter (both target)
#
        c = [1]*len(buttons)
        A = [[i in b for b in buttons] for i in range(len(target))]
        total_presses += scipy.optimize.milp(c,constraints=[A, target, target],integrality=c).fun

print('Result for', datafile, '=', total_presses)
print('Runtime: %s seconds.' % (time.time() - start_time))