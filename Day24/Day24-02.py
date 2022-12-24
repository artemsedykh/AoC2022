field = []

with open('day24.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        field.append(list(line))
        line = file.readline().strip()

h, w = len(field) - 2, len(field[0]) - 2


def gcd(a, b):
    if a > b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a


period = h * w // gcd(h, w)

blizz = set()
for row in range(1, h + 1):
    for col in range(1, w + 1):
        if field[row][col] in '<>^v':
            blizz.add((row, col, field[row][col]))

field_stat = dict()
for i in range(period):
    field_stat[i] = blizz
    next_blizz = set()
    for b in blizz:
        row, col, move = b
        if move == '<':
            if 1 < col:
                next_blizz.add((row, col - 1, move))
            else:
                next_blizz.add((row, w, move))
        elif move == '^':
            if 1 < row:
                next_blizz.add((row - 1, col, move))
            else:
                next_blizz.add((h, col, move))
        elif move == '>':
            if col < w:
                next_blizz.add((row, col + 1, move))
            else:
                next_blizz.add((row, 1, move))
        elif move == 'v':
            if row < h:
                next_blizz.add((row + 1, col, move))
            else:
                next_blizz.add((1, col, move))
    blizz = next_blizz

start = (0, 1)
end = (h + 1, w)
steps = 0


def go(start, end, steps):
    last_c = set()
    last_c.add(start)
    while not end in last_c:
        new_c = set()
        blizz = field_stat[(steps + 1) % period]
        for c in last_c:
            row, col = c
            dblock = row == h + 1 or (row == h and col != w) or (row + 1, col, '<') in blizz or (
                row + 1, col, '>') in blizz or (
                         row + 1, col, '^') in blizz
            rblock = row in (0, h + 1) or col >= w or (row, col + 1, '<') in blizz or (row, col + 1, '^') in blizz or (
                row, col + 1, 'v') in blizz
            ublock = row == 0 or (row == 1 and col != 1) or (row - 1, col, '<') in blizz or (
                row - 1, col, '>') in blizz or (
                         row - 1, col, 'v') in blizz
            lblock = row in (0, h + 1) or col <= 1 or (row, col - 1, '>') in blizz or (row, col - 1, '^') in blizz or (
                row, col - 1, 'v') in blizz
            wblock = (row, col, '<') in blizz or (row, col, '>') in blizz or (row, col, '^') in blizz or (
                row, col, 'v') in blizz
            if not dblock:
                new_c.add((row + 1, col))
            if not rblock:
                new_c.add((row, col + 1))
            if not ublock:
                new_c.add((row - 1, col))
            if not lblock:
                new_c.add((row, col - 1))
            if not wblock:
                new_c.add((row, col))
        last_c = new_c
        steps += 1
    return steps


steps = go(start, end, go(end, start, go(start, end, steps)))
print(steps)
