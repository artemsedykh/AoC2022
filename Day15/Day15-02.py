def mdist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

sensors, beacons = [], []

pb = dict()
MAX_COORD = 4_000_000

for i in range(0, MAX_COORD+1):
    pb[i] = [(0, MAX_COORD)]

def intersect(segments, y):
    res = []
    for s in segments:
        if s[1] < y[0] or y[1] < s[0]:
            res.append(s)
        elif s[0] < y[0] <= s[1] <= y[1]:
            res.append((s[0], y[0]-1))
        elif y[0] <= s[0] <= y[1] < s[1]:
            res.append((y[1]+1, s[1]))
        elif s[0] < y[0] <= y[1] < s[1]:
            res.append((s[0], y[0]-1))
            res.append((y[1]+1, s[1]))
        elif y[0] <= s[0] <= s[1] <= y[1]:
            pass
    return res


def set_no_beacons(sx, sy, bx, by):
    dist = mdist(sx, sy, bx, by)
    x = max(sx-dist, 0)
    dy = dist - (sx - x)
    while x <= min(sx+dist, MAX_COORD):
        if x in pb.keys():
            res = intersect(pb[x], (sy-dy, sy+dy))
            if res:
                pb[x] = res
            else:
                pb.pop(x)
        dy = dy + 1 if x < sx else dy - 1
        x += 1


with open('day15.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        sline = line.replace(',', '').replace(':', '').split()
        sx, sy, bx, by = int(sline[2][2:]), int(sline[3][2:]), int(sline[8][2:]), int(sline[9][2:])
        sensors.append((sx, sy))
        beacons.append((bx, by))
        set_no_beacons(sx, sy, bx, by)
        line = file.readline().strip()

key = list(pb.keys())[0]
print(key*4_000_000+pb[key][0][0])