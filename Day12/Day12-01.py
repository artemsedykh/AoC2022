with open('day12.txt', 'r') as file:
    field = []
    line = file.readline().strip()
    while line:
        field.append(line)
        line = file.readline().strip()

max_x = len(field) - 1
max_y = len(field[0]) - 1

Spos = (0, 0)
Epos = (0, 0)
for i in range(max_x + 1):
    if field[i].find('S') > -1:
        Spos = (i, field[i].find('S'))
        field[i] = field[i].replace('S', 'a')
    if field[i].find('E') > -1:
        Epos = (i, field[i].find('E'))
        field[i] = field[i].replace('E', 'z')

max_p = (max_x + 1) * (max_y + 1)

pole = []
for _ in range(max_x + 1):
    pole.append([max_p for i in range(max_y + 1)])


def new_val(i, j):
    left, right, up, down = [max_p] * 4
    if i > 0 and ord(field[i - 1][j]) - ord(field[i][j]) <= 1:
        up = pole[i - 1][j]
    if i < max_x and ord(field[i + 1][j]) - ord(field[i][j]) <= 1:
        down = pole[i + 1][j]
    if j > 0 and ord(field[i][j - 1]) - ord(field[i][j]) <= 1:
        left = pole[i][j - 1]
    if j < max_y and ord(field[i][j + 1]) - ord(field[i][j]) <= 1:
        right = pole[i][j + 1]
    return min(min(up, down, left, right) + 1, max_p)


x, y = Epos
pole[x][y] = 0

path = []
for s in range(1, max(max_x, max_y) + 2):
    i = x
    j = y - s
    while j < y:
        if 0 <= i <= max_x and 0 <= j <= max_y:
            path.append((i, j))
        i -= 1
        j += 1
    while i < x:
        if 0 <= i <= max_x and 0 <= j <= max_y:
            path.append((i, j))
        i += 1
        j += 1
    while j > y:
        if 0 <= i <= max_x and 0 <= j <= max_y:
            path.append((i, j))
        i += 1
        j -= 1
    while i > x:
        if 0 <= i <= max_x and 0 <= j <= max_y:
            path.append((i, j))
        i -= 1
        j -= 1

for k in range(max(max_x, max_y)+1):
    for cell in path:
        i, j = cell
        pole[i][j] = new_val(i, j)

print(pole[Spos[0]][Spos[1]])