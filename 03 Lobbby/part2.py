import os

datafile = "input.txt"

joltage = 0
battery_count = 12

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for line in input:
        bank_jolts = ''
        start = 0
        for bat in range(battery_count):
            bat_list = line[start:bat - battery_count]
            bat_jolts = max(bat_list)
            bat_pos = bat_list.index(bat_jolts)
            bank_jolts += bat_jolts
            start += bat_pos + 1
        joltage += int(bank_jolts)
        
print('Result = ', joltage)