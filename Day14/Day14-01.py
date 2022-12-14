cave_coords = []

with open('day14.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        cave_coords.append([list(map(int, s.split(','))) for s in line.split(' -> ')])
        line = file.readline().strip()

max_x, max_y, min_x, min_y = *cave_coords[0][0], *cave_coords[0][0]

for row in cave_coords:
    for coord in row:
        max_x = max(max_x, coord[0])
        max_y = max(max_y, coord[1])
        min_x = min(min_x, coord[0])
        min_y = min(min_y, coord[1])


cave = []
for i in range(max_y + 2):
    cave.append(['.' for j in range(max_x + 2)])
cave.append(['#' for j in range(max_x + 2)])

for row in cave_coords:
    i = 1
    while i < len(row):
        prev, curr = row[i - 1], row[i]
        if prev[0] == curr[0]:
            if prev[1] < curr[1]:
                for k in range(prev[1], curr[1] + 1):
                    cave[k][prev[0]] = '#'
            else:
                for k in range(prev[1], curr[1] - 1, -1):
                    cave[k][prev[0]] = '#'
        else:
            if prev[0] < curr[0]:
                for k in range(prev[0], curr[0] + 1):
                    cave[prev[1]][k] = '#'
            else:
                for k in range(prev[0], curr[0] - 1, -1):
                    cave[prev[1]][k] = '#'
        i += 1

# simulate sand
count = 0
y, x = 0, 500
while y < max_y:
    falling = True
    y, x = 0, 500
    while falling and y < max_y:
        if cave[y+1][x] == '.':
            y += 1
        elif cave[y+1][x-1] == '.':
            x, y = x - 1, y + 1
        elif cave[y+1][x+1] == '.':
            x, y = x + 1, y + 1
        else:
            cave[y][x] = 'o'
            falling = False
            count += 1


print(count)
