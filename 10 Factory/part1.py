import os

datafile = "input.txt"

total_presses = 0

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for line in input:
        row = line[0:-1].split()
        # Convert target light state to binary
        target_str = row[0][1:-1]
        target = 0b0
        for n in range(len(target_str)):
            target += 2**n if target_str[n] == '#' else 0
        # Convert buttons to binary
        buttons = set()
        for button_str in row[1:-1]:
            button = 0b0
            for n_str in button_str[1:-1].split(','):
                button += 2**int(n_str)
            buttons.add(button)
        # Maintain prune set of light states already reached
        prune_set = set()
        # Breadth-first search to reach target state
        search_states = {0b0}
        press_count = 0
        while not target in search_states:
            press_count += 1
            next_states = set()
            for state in search_states:
                prune_set.add(state)
                for button in buttons:
                    next = state ^ button
                    if next not in prune_set:
                        next_states.add(next)
            search_states = next_states.copy()
        total_presses += press_count

print('Result = ', total_presses)