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
    next_pos = next(curr_dir, curr_pos)
    while steps > 0 and is_not_wall(next_pos):
        curr_pos = next_pos
        steps -= 1
        next_pos = next(curr_dir, curr_pos)
    return curr_pos


def next(curr_dir, curr_pos):
    row, col = curr_pos
    if curr_dir == 0:
        return (row, col + 1) if col + 1 <= monkey_map[row][1] else (row, monkey_map[row][0])
    if curr_dir == 1:
        if row + 1 < len(monkey_map) and monkey_map[row + 1][0] <= col <= monkey_map[row + 1][1]:
            return row + 1, col
        else:
            i = 0
            while not monkey_map[i][0] <= col <= monkey_map[i][1]:
                i += 1
            return i, col
    if curr_dir == 2:
        return (row, col - 1) if monkey_map[row][0] <= col - 1 else (row, monkey_map[row][1])
    if curr_dir == 3:
        if row - 1 >= 0 and monkey_map[row - 1][0] <= col <= monkey_map[row - 1][1]:
            return row - 1, col
        else:
            i = len(monkey_map) - 1
            while not monkey_map[i][0] <= col <= monkey_map[i][1]:
                i -= 1
            return i, col


def is_not_wall(pos):
    return not pos[1] in monkey_map[pos[0]][2]


moves = ['E', 'S', 'W', 'N']
curr_dir = 0
curr_pos = (0, monkey_map[0][0])
str_steps = ''
for s in path:
    if s in 'LR':
        curr_pos = go(curr_dir, curr_pos, int(str_steps))
        curr_dir = (curr_dir + 1) % len(moves) if s == 'R' else (curr_dir - 1) % len(moves)
        str_steps = ''
    else:
        str_steps += s
curr_pos = go(curr_dir, curr_pos, int(str_steps))

print((curr_pos[0] + 1) * 1000 + (curr_pos[1] + 1) * 4 + curr_dir)
