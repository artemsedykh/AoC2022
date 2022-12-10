CRT = [['.' for i in range(40)] for j in range(6)]

def draw_pixel(cycle, X):
    if cycle < 240 and cycle % 40 in (X-1, X, X+1):
        CRT[cycle // 40][cycle % 40] = '#'


with open('day10.txt', 'r') as file:
    line = file.readline().strip()
    X = 1
    cycle = 0
    while line:
        if line[:4] == 'noop':
            cycle += 1
            draw_pixel(cycle, X)
        else:
            num = int(line.split()[1])
            cycle += 1
            draw_pixel(cycle, X)
            cycle += 1
            X += num
            draw_pixel(cycle, X)
        line = file.readline().strip()

for row in CRT:
    print("".join(row))