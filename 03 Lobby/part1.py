import os

datafile = "input.txt"

joltage = 0

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for line in input:
        bat1_jolts = max(line[:-2])
        bat1_pos = line[:-2].index(bat1_jolts)
        bat2_jolts = max(line[bat1_pos + 1:-1])
        joltage += int(bat2_jolts) + int(bat1_jolts) * 10
        
print('Result = ', joltage)