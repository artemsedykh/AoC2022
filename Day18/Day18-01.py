scanned = set()
acc = 0

def count(acc, x, y, z):
    acc += 6
    c_to_scan = [
        (x-1, y, z),
        (x+1, y, z),
        (x, y-1, z),
        (x, y+1, z),
        (x, y, z-1),
        (x, y, z+1)
    ]
    for c in c_to_scan:
        if c in scanned:
            acc -= 2
    return acc



with open('day18.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        coords = tuple(map(int, [s for s in line.split(',')]))
        acc = count(acc, *coords)
        scanned.add(coords)
        line = file.readline().strip()

print(acc)