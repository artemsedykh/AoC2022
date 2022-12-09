woods = []

with open('day08.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        woods.append([int(tree) for tree in line])
        line = file.readline().strip()

l = len(woods)
max_vis = 0
for i in range(1, l-1):
    for j in range(1, l-1):
        acc1, acc2, acc3, acc4 = 0, 0, 0, 0

        # go left
        x, y = i-1, j
        while x >= 0 and woods[i][j] > woods[x][y]:
            acc1 += 1
            x -= 1
        acc1 = acc1 + 1 if x != -1 else acc1
        # go right
        x, y = i+1, j
        while x < l and woods[i][j] > woods[x][y]:
            acc2 += 1
            x += 1
        acc2 = acc2 + 1 if x != l else acc2
        # go up
        x, y = i, j-1
        while y >= 0 and woods[i][j] > woods[x][y]:
            acc3 += 1
            y -= 1
        acc3 = acc3 + 1 if y != -1 else acc3
        # go down
        x, y = i, j+1
        while y < l and woods[i][j] > woods[x][y]:
            acc4 += 1
            y += 1
        acc4 = acc4 + 1 if y != l else acc4
        max_vis = max(max_vis, acc1*acc2*acc3*acc4)
        if max_vis == acc1*acc2*acc3*acc4:
            print(i, j, acc1, acc2, acc3, acc4)

print(max_vis)