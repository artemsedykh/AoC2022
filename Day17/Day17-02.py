MAX_ROCKS = 1_000_000_000_000
# MAX_ROCKS = 76

with open('day17example.txt', 'r') as file:
    jet = file.readline().strip()

rocks = {
    0: {
        'bottom': [(0, 2), (0, 3), (0, 4), (0, 5)],
        'left': [(0, 2)],
        'right': [(0, 5)],
        'render': [(0, 2), (0, 3), (0, 4), (0, 5)]
    },
    1: {
        'bottom': [(1, 2), (0, 3), (1, 4)],
        'left': [(1, 2), (0, 3), (2, 3)],
        'right': [(1, 4), (0, 3), (2, 3)],
        'render': [(1, 2), (0, 3), (1, 3), (2, 3), (1, 4)]
    },
    2: {
        'bottom': [(0, 2), (0, 3), (0, 4)],
        'left': [(0, 2), (1, 4), (2, 4)],
        'right': [(0, 4), (1, 4), (2, 4)],
        'render': [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)]
    },
    3: {
        'bottom': [(0, 2)],
        'left': [(0, 2), (1, 2), (2, 2), (3, 2)],
        'right': [(0, 2), (1, 2), (2, 2), (3, 2)],
        'render': [(0, 2), (1, 2), (2, 2), (3, 2)]
    },
    4: {
        'bottom': [(0, 2), (0, 3)],
        'left': [(0, 2), (1, 2)],
        'right': [(0, 3), (1, 3)],
        'render': [(0, 2), (1, 2), (0, 3), (1, 3)]
    }
}

start = 371
period = 2673

chamber = [['#' for i in range(7)]]
for r in range(start + int(period * 3)):
    chamber.append(['.' for i in range(7)])
def print_ch():
    for i in range(curr, 0, -1):
        print("".join(chamber[i]))
    print()


def move_rock(rock, x, y):
    for key in rock.keys():
        rock[key] = [(p[0] + x, p[1] + y) for p in rock[key]]
    return rock


curr, rem_curr = 0, 0
i, j = 0, 0

while curr < start:
    rnum = i % len(rocks.keys())
    rock = rocks[rnum].copy()
    rock = move_rock(rock, curr + 4, 0)
    moving = True
    while moving:
        nextj = jet[j % len(jet)]
        if nextj == '<' and rock['bottom'][0][1] > 0:
            movl = True
            for p in rock['left']:
                movl = movl and (chamber[p[0]][p[1] - 1] == '.')
            if movl:
                rock = move_rock(rock, 0, -1)
        if nextj == '>' and rock['bottom'][-1][1] < 6:
            movr = True
            for p in rock['right']:
                movr = movr and (chamber[p[0]][p[1] + 1] == '.')
            if movr:
                rock = move_rock(rock, 0, 1)
        for p in rock['bottom']:
            moving = moving and (chamber[p[0] - 1][p[1]] == '.')
        if moving:
            rock = move_rock(rock, -1, 0)
        j += 1
    for p in rock['render']:
        chamber[p[0]][p[1]] = '#'
    for k in range(curr, curr + 5):
        if '#' in chamber[k]:
            curr = k
    i += 1

start_rocks = i
start_curr = curr
curr_rocks = []

while curr < start + period:
    curr_rocks.append(curr)
    rnum = i % len(rocks.keys())
    rock = rocks[rnum].copy()
    rock = move_rock(rock, curr + 4, 0)
    moving = True
    while moving:
        nextj = jet[j % len(jet)]
        if nextj == '<' and rock['bottom'][0][1] > 0:
            movl = True
            for p in rock['left']:
                movl = movl and (chamber[p[0]][p[1] - 1] == '.')
            if movl:
                rock = move_rock(rock, 0, -1)
        if nextj == '>' and rock['bottom'][-1][1] < 6:
            movr = True
            for p in rock['right']:
                movr = movr and (chamber[p[0]][p[1] + 1] == '.')
            if movr:
                rock = move_rock(rock, 0, 1)
        for p in rock['bottom']:
            moving = moving and (chamber[p[0] - 1][p[1]] == '.')
        if moving:
            rock = move_rock(rock, -1, 0)
        j += 1
    for p in rock['render']:
        chamber[p[0]][p[1]] = '#'
    for k in range(curr, curr + 5):
        if '#' in chamber[k]:
            curr = k
    i += 1

period_rocks = i - start_rocks

num_periods = (MAX_ROCKS - start_rocks) // period_rocks
remainder = (MAX_ROCKS - start_rocks) % period_rocks

print(num_periods * (curr - start_curr) + curr_rocks[remainder])
