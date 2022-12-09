with open('day09.txt', 'r') as file:
    data = []
    line = file.readline().strip()
    while line:
        direct, steps = line.split()
        data.append([direct, int(steps)])
        line = file.readline().strip()

max_moves = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
for d in data:
    max_moves[d[0]] += d[1]

field = []
for _ in range(max_moves['U'] + max_moves['D'] + 1):
    field.append([0 for j in range(max_moves['L'] + max_moves['R'] + 1)])


def check_coord(hx, hy, tx, ty):
    return (abs(hx - tx) > 1) or (abs(hy - ty) > 1)


def sgn(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    return 0


def move_t(hx, hy, tx, ty):
    if abs(hx-tx) == 2 and abs(hy-ty) == 1:
        tx = hx - sgn(hx - tx)
        ty = hy
    elif abs(hx-tx) == 1 and abs(hy-ty) == 2:
        tx = hx
        ty = hy - sgn(hy - ty)
    else:
        tx = hx - sgn(hx - tx)
        ty = hy - sgn(hy - ty)
    return tx, ty


def move_h(hx, hy, d):
    if d == 'D':
        return hx + 1, hy
    elif d == 'U':
        return hx - 1, hy
    elif d == 'L':
        return hx, hy - 1
    elif d == 'R':
        return hx, hy + 1


hx, tx = [max_moves['U'] + 1] * 2
hy, ty = [max_moves['L'] + 1] * 2

for d in data:
    for _ in range(d[1]):
        hx, hy = move_h(hx, hy, d[0])
        if check_coord(hx, hy, tx, ty):
            field[tx][ty] = 1
            tx, ty = move_t(hx, hy, tx, ty)
field[tx][ty] = 1

acc = 0
for row in field:
    for col in row:
        acc += col
print(acc)
