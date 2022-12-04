with open('day02.txt', 'r') as file:
    data = [list(x.split()) for x in file.read().split('\n')]


def add_score(a: str, b: str) -> int:
    moves = ['X', 'Y', 'Z']
    wins = [('C', 'X'), ('A', 'Y'), ('B', 'Z')]
    draws = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
    score = moves.index(b) + 1
    if (a, b) in wins:
        score += 6
    elif (a, b) in draws:
        score += 3
    return score


total_score = 0
for move in data:
    total_score += add_score(*move)

print(total_score)
