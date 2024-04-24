def print_crt(crt):
    for row in crt:
        print("".join(row))


puzzle_input = open("day_10_data.txt").read().strip()
puzzle_rows = puzzle_input.splitlines()

cmd_count = 0
cycle = 0
x_reg = 1
signal_lst = []
signal_start = 20
signal_step = 40

crt = ['.'*240]
crt = [['.']*40 for i in range(6)]
RunningCommand = False

while True:
    cycle += 1

    if (cycle-signal_start) % signal_step == 0:
        signal_lst.append(x_reg * cycle)

    cmd = puzzle_rows[cmd_count]
    if cmd == 'noop':
        cmd_count += 1
    else:
        if not RunningCommand:
            RunningCommand = True
        else:
            _, value = cmd.split(" ")
            x_reg += int(value)
            cmd_count += 1
            RunningCommand = False

    sprite = cycle % 40
    row = int(cycle / 40)
    if x_reg-1 <= sprite <= x_reg+1:
        crt[row][sprite-1] = '#'

    if cmd_count >= len(puzzle_rows):
        break

print(sum(signal_lst))
print_crt(crt)
