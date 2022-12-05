with open('day05.txt', 'r') as file:
    storage, moves = [], []
    line = file.readline().strip()
    while line:
        storage.append(line)
        line = file.readline().strip()
    line = file.readline().strip()
    while line:
        moves.append(line)
        line = file.readline().strip()

# rearrange storage to crates
crates_nums = list(map(int, storage[-1].split()))
crates = dict(zip(crates_nums, [[] for i in crates_nums]))
for line_num in range(-2, -len(storage) - 1, -1):
    storage_line = storage[line_num]
    j = 0
    pos = j * 4 + 1
    while pos < len(storage_line):
        if storage_line[pos] == " ":
            pass
        else:
            crates[j + 1].append(storage_line[pos])
        j += 1
        pos = j * 4 + 1


def move_crates(move):
    quantity, move_from, move_to = [int(s) for s in move.split() if s.isdigit()]
    for _ in range(quantity):
        crate = crates[move_from].pop()
        crates[move_to].append(crate)


for move in moves:
    move_crates(move)

top_crates = [crates[c][-1] for c in crates]
print("".join(top_crates))
