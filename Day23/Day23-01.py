elves = set()
with open('day23.txt', 'r') as file:
    row = 0
    line = file.readline().strip()
    while line:
        for col in range(len(line)):
            if line[col] == '#':
                elves.add((row, col))
        row += 1
        line = file.readline().strip()


def are_elves_around(elf):
    row, col = elf
    return (row - 1, col - 1) in elves or (row - 1, col) in elves or (row - 1, col + 1) in elves or \
        (row, col - 1) in elves or (row, col + 1) in elves or (row + 1, col - 1) in elves or \
        (row + 1, col) in elves or (row + 1, col + 1) in elves


def next(round, elf):
    moves = ['N', 'S', 'W', 'E']
    row, col = elf
    for i in range(4):
        move = moves[(i + round) % 4]
        if move == 'N':
            if not ((row - 1, col - 1) in elves or (row - 1, col) in elves or (row - 1, col + 1) in elves):
                return row - 1, col
        elif move == 'S':
            if not ((row + 1, col - 1) in elves or (row + 1, col) in elves or (row + 1, col + 1) in elves):
                return row + 1, col
        elif move == 'W':
            if not ((row - 1, col - 1) in elves or (row, col - 1) in elves or (row + 1, col - 1) in elves):
                return row, col - 1
        elif move == 'E':
            if not ((row - 1, col + 1) in elves or (row, col + 1) in elves or (row + 1, col + 1) in elves):
                return row, col + 1
    return row, col


def count_empty_tiles():
    minr, minc, maxr, maxc = 1000, 1000, -1000, -1000
    for elf in elves:
        row, col = elf
        minr = min(minr, row)
        maxr = max(maxr, row)
        minc = min(minc, col)
        maxc = max(maxc, col)
    return (maxr - minr + 1) * (maxc - minc + 1) - len(elves)


moves_elf_d = dict()
for i in range(10):
    for elf in elves:
        if are_elves_around(elf):
            next_move = next(i, elf)
            if next_move in moves_elf_d.keys():
                moves_elf_d[next_move].append(elf)
            else:
                moves_elf_d[next_move] = []
                moves_elf_d[next_move].append(elf)
        else:
            moves_elf_d[elf] = []
            moves_elf_d[elf].append(elf)
    new_elf_map = set()
    for move in moves_elf_d.keys():
        if len(moves_elf_d[move]) == 1:
            new_elf_map.add(move)
        else:
            for _ in moves_elf_d[move]:
                new_elf_map.add(_)
    elves = new_elf_map
    moves_elf_d = dict()

print(count_empty_tiles())
