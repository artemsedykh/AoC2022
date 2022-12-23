monkey_map = []
path = ''
with open('day22.txt', 'r') as file:
    line = file.readline()
    while line != '\n':
        lborder, rborder = -1, len(line) - 1
        walls = set()
        for i in range(len(line)):
            if line[i] == '.':
                lborder = i if lborder == -1 else lborder
            elif line[i] == '#':
                lborder = i if lborder == -1 else lborder
                walls.add(i)
            elif i > 0:
                rborder = i - 1 if lborder != -1 and line[i - 1] in '.#' else rborder
        monkey_map.append([lborder, rborder, walls])
        line = file.readline()
    path = file.readline()


def go(curr_dir, curr_pos, steps):
    next_dir, next_pos = next(curr_dir, curr_pos)
    while steps > 0 and is_not_wall(next_pos):
        curr_dir, curr_pos = next_dir, next_pos
        # pathe.append([str(curr_dir), curr_pos])
        steps -= 1
        next_dir, next_pos = next(curr_dir, curr_pos)
    return curr_dir, curr_pos


def next(curr_dir, curr_pos):
    row, col = curr_pos
    if curr_dir == 0:
        if col + 1 <= monkey_map[row][1]:
            return curr_dir, (row, col + 1)
        elif 0 <= row <= 49:
            return 2, (149 - row, 99)
        elif 50 <= row <= 99:
            return 3, (49, row + 50)
        elif 100 <= row <= 149:
            return 2, (149 - row, 149)
        elif 150 <= row <= 199:
            return 3, (149, row - 100)
    if curr_dir == 1:
        if row + 1 < len(monkey_map) and monkey_map[row + 1][0] <= col <= monkey_map[row + 1][1]:
            return curr_dir, (row + 1, col)
        elif 0 <= col <= 49:
            return 1, (0, col + 100)
        elif 50 <= col <= 99:
            return 2, (col + 100, 49)
        elif 100 <= col <= 149:
            return 2, (col - 50, 99)
    if curr_dir == 2:
        if monkey_map[row][0] <= col - 1:
            return curr_dir, (row, col - 1)
        elif 0 <= row <= 49:
            return 0, (149 - row, 0)
        elif 50 <= row <= 99:
            return 1, (100, row - 50)
        elif 100 <= row <= 149:
            return 0, (149 - row, 50)
        elif 150 <= row <= 199:
            return 1, (0, row - 100)
    if curr_dir == 3:
        if row - 1 >= 0 and monkey_map[row - 1][0] <= col <= monkey_map[row - 1][1]:
            return curr_dir, (row - 1, col)
        elif 0 <= col <= 49:
            return 0, (col + 50, 50)
        elif 50 <= col <= 99:
            return 0, (col + 100, 0)
        elif 100 <= col <= 149:
            return 3, (199, col - 100)


def is_not_wall(pos):
    return not pos[1] in monkey_map[pos[0]][2]


moves = ['E', 'S', 'W', 'N']
curr_dir = 0
curr_pos = (0, monkey_map[0][0])
str_steps = ''
for s in path:
    if s in 'LR':
        curr_dir, curr_pos = go(curr_dir, curr_pos, int(str_steps))
        curr_dir = (curr_dir + 1) % len(moves) if s == 'R' else (curr_dir - 1) % len(moves)
        str_steps = ''
    else:
        str_steps += s
curr_dir, curr_pos = go(curr_dir, curr_pos, int(str_steps))

print((curr_pos[0] + 1) * 1000 + (curr_pos[1] + 1) * 4 + curr_dir)
