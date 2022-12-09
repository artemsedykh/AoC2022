with open('day09.txt', 'r') as file:
    data = []
    line = file.readline().strip()
    while line:
        direct, steps = line.split()
        data.append([direct, int(steps)])
        line = file.readline().strip()


def check_coord(hx, hy, tx, ty):
    return (abs(hx - tx) > 1) or (abs(hy - ty) > 1)


def sgn(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    return 0


def move_t(hx, hy, tx, ty):
    if abs(hx - tx) == 2 and abs(hy - ty) == 1:
        tx = hx - sgn(hx - tx)
        ty = hy
    elif abs(hx - tx) == 1 and abs(hy - ty) == 2:
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


path = set()
hrope = [[0, 0] for _ in range(10)]

for d in data:
    for _ in range(d[1]):
        hrope[0][0], hrope[0][1] = move_h(hrope[0][0], hrope[0][1], d[0])
        for knot in range(1, 10):
            if check_coord(hrope[knot - 1][0], hrope[knot - 1][1], hrope[knot][0], hrope[knot][1]):
                if knot == 9:
                    path.add((hrope[knot][0], hrope[knot][1]))
                hrope[knot][0], hrope[knot][1] = move_t(hrope[knot - 1][0], hrope[knot - 1][1], hrope[knot][0],
                                                        hrope[knot][1])
path.add((hrope[knot][0], hrope[knot][1]))

print(len(path))