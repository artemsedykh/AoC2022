def mdist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


no_beacons = set()
sensors, beacons = [], []


def set_no_beacons(sx, sy, bx, by):
    d = mdist(sx, sy, bx, by)
    for x in range(sx - d, sx + d + 1):
        if mdist(x, 2_000_000, sx, sy) <= d:
            no_beacons.add((x, 2_000_000))


with open('day15.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        sline = line.replace(',', '').replace(':', '').split()
        sx, sy, bx, by = int(sline[2][2:]), int(sline[3][2:]), int(sline[8][2:]), int(sline[9][2:])
        sensors.append((sx, sy))
        beacons.append((bx, by))
        set_no_beacons(sx, sy, bx, by)
        line = file.readline().strip()

acc = 0
for coord in no_beacons:
    if not coord in sensors and not coord in beacons:
        acc += 1

print(acc)
