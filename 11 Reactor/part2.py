import os, time, datetime

start_time = time.time()
print('Started:', datetime.datetime.now().time())

datafile = "input.txt"

def dfs(devices, stack, end):
    count = 0
    while stack:
        device = stack.pop()
        if device == end:
            count += 1
        elif device in devices:
            stack.extend(devices[device])
    return count

def prune(dict, target):
    # Return a pruned dictionary that only includes ancestors of target
    new_dict = {}
    copylist = [k for k, v in dict.items() if target in v]
    while copylist:
        entry = copylist.pop()
        if entry not in new_dict:
            new_dict[entry] = dict[entry]
            copylist.extend([k for k, v in dict.items() if entry in v])
    return new_dict

devices = {}

# Build dictionary of each device and the devices it's connected to.
with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for line in input:
        row = line[0:-1].split(': ')
        devices[row[0]] = row[1].split()

# There are no dac-to-fft paths in the data, so we can split the search into three stages:
# svr-to-fft, fft-ro-dac, and dac-to-out
fft_dict = prune(devices, 'fft')
stage1 = dfs(fft_dict, ['svr'], 'fft')
print('Checkpoint 1: %s seconds.' % (time.time() - start_time))
dac_dict = prune(devices, 'dac')
stage2 = dfs(dac_dict, ['fft'], 'dac')
print('Checkpoint 2: %s seconds.' % (time.time() - start_time))
out_dict = prune(devices, 'out')
stage3 = dfs(out_dict, ['dac'], 'out')

path_count = stage1 * stage2 * stage3

print('Result for', datafile, '=', path_count)
print('Runtime: %s seconds.' % (time.time() - start_time))