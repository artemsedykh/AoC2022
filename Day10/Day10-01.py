def add_signal_strength(acc, cycle, X):
    needed_cycles = [20, 60, 100, 140, 180, 220]
    return acc + cycle * X if cycle in needed_cycles else acc


with open('day10.txt', 'r') as file:
    line = file.readline().strip()
    X = 1
    cycle = 1
    acc = 0
    while line:
        if line[:4] == 'noop':
            cycle += 1
            acc = add_signal_strength(acc, cycle, X)
        else:
            num = int(line.split()[1])
            cycle += 1
            acc = add_signal_strength(acc, cycle, X)
            cycle += 1
            X += num
            acc = add_signal_strength(acc, cycle, X)
        line = file.readline().strip()

print(acc)