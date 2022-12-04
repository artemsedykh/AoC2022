with open('day02.txt', 'r') as file:
    data = [list(x.split()) for x in file.read().split('\n')]


def add_score(a, b):
    moves = ['A', 'B', 'C']
    bmove = ''
    score = 0
    if b == 'X':
        bmove = moves[(moves.index(a) - 1) % 3]
    elif b == 'Y':
        bmove = a
        score += 3
    elif b == 'Z':
        bmove = moves[(moves.index(a) + 1) % 3]
        score += 6
    score += moves.index(bmove) + 1
    return score


total_score = 0
for move in data:
    total_score += add_score(*move)

print(total_score)
