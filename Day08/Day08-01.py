woods = []

with open('day08.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        woods.append([int(tree) for tree in line])
        line = file.readline().strip()

l = len(woods)
center = (l + 1) // 2

vis = []
for i in range(l):
    if i in (0, l-1):
        vis.append([True for _ in range(l)])
    else:
        vis.append([True] + [False for _ in range(1, l-1)] + [True])

# left -> right
for i in range(l):
    highest = -1
    for j in range(l):
        if woods[i][j] > highest:
            vis[i][j] = True
            highest = woods[i][j]

# right -> left
for i in range(l):
    highest = -1
    for j in range(l-1, -1, -1):
        if woods[i][j] > highest:
            vis[i][j] = True
            highest = woods[i][j]

# top -> bottom
for i in range(l):
    highest = -1
    for j in range(l):
        if woods[j][i] > highest:
            vis[j][i] = True
            highest = woods[j][i]

# bottom -> top
for i in range(l):
    highest = -1
    for j in range(l-1, -1, -1):
        if woods[j][i] > highest:
            vis[j][i] = True
            highest = woods[j][i]

acc = 0
for row in vis:
    for col in row:
        acc = acc + 1 if col else acc

print(acc)