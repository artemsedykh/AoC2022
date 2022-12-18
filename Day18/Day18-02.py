scanned = set()
acc = 0


def count(acc, x, y, z):
    acc += 6
    c_to_scan = [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1)
    ]
    for c in c_to_scan:
        if c in scanned:
            acc -= 2
    return acc


scanned_air = set()
acc_air = 0


def count_air(acc, x, y, z):
    acc += 6
    c_to_scan = [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1)
    ]
    for c in c_to_scan:
        if c in scanned_air:
            acc -= 2
    return acc


def scan_for_ext(x, y, z):
    c_to_scan = [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1)
    ]
    for c in c_to_scan:
        if volc[c[0]][c[1]][c[2]] == 2:
            return True
    return False


xmax, ymax, zmax = 0, 0, 0

with open('day18.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        coords = tuple(map(int, [s for s in line.split(',')]))
        acc = count(acc, *coords)
        scanned.add(coords)
        xmax, ymax, zmax = max(xmax, coords[0]), max(ymax, coords[1]), max(zmax, coords[2])
        line = file.readline().strip()

volc = []
for x in range(0, xmax + 1):
    slice = []
    for y in range(0, ymax + 1):
        row = []
        for z in range(0, zmax + 1):
            if (x, y, z) in scanned:
                row.append(1)
            else:
                if x in (0, xmax) or y in (0, ymax) or z in (0, zmax):
                    row.append(2)
                else:
                    row.append(0)
        slice.append(row)
    volc.append(slice)

for x in range(1, xmax):
    for y in range(1, ymax):
        for z in range(1, zmax):
            c_to_check = [(x, y, z), (x, y, zmax - z), (x, ymax - y, z), (x, ymax - y, zmax - y),
                          (xmax - x, y, z), (xmax - x, y, zmax - z), (xmax - x, ymax - y, z),
                          (xmax - x, ymax - y, zmax - y)]
            for c in c_to_check:
                if volc[c[0]][c[1]][c[2]] == 0 and scan_for_ext(*c):
                    volc[c[0]][c[1]][c[2]] = 2

for x in range(0, xmax + 1):
    for y in range(0, ymax + 1):
        for z in range(0, zmax + 1):
            if volc[x][y][z] == 0:
                acc_air = count_air(acc_air, x, y, z)
                scanned_air.add((x, y, z))

print(acc - acc_air)
