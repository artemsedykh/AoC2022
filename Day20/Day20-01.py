seq = []


def remainder(k, l):
    if k >= 0:
        return k % (l - 1)
    else:
        return -(-k % (l - 1))


with open('day20.txt', 'r') as file:
    i = 0
    line = file.readline()
    while line:
        seq.append([int(line), i])
        line = file.readline()
        i += 1

l = len(seq)

# print([s[0] for s in seq])
# print()


for i in range(l):
    j = 0
    while j < l:
        if seq[j][1] == i:
            break
        j += 1
    old_pos = j
    val = seq[old_pos][0]
    new_pos = old_pos + remainder(val, l)
    if new_pos <= 0 and val < 0:
        new_pos = (new_pos - 1) % l
    if new_pos >= l and val > 0:
        new_pos = (new_pos + 1) % l
    if old_pos < new_pos:
        new_seq = seq[:old_pos] + seq[old_pos + 1:new_pos + 1] + [seq[old_pos]] + seq[new_pos + 1:]
        seq = new_seq
    elif old_pos > new_pos:
        new_seq = seq[:new_pos] + [seq[old_pos]] + seq[new_pos:old_pos] + seq[old_pos + 1:]
        seq = new_seq

for i in range(l):
    if seq[i][0] == 0:
        break
pos1k = (i + 1000) % l
pos2k = (i + 2000) % l
pos3k = (i + 3000) % l
print(pos1k, seq[pos1k][0], pos2k, seq[pos2k][0], pos3k, seq[pos3k][0])
print(seq[pos1k][0] + seq[pos2k][0] + seq[pos3k][0])
