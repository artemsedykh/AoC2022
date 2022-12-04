import string

with open('day03.txt', 'r') as file:
    data = file.read().split()

# set priorities
prio = {}
for c in string.ascii_lowercase:
    prio[c] = ord(c) - ord('a') + 1
for c in string.ascii_uppercase:
    prio[c] = ord(c) - ord('A') + 27


def rep_item_prio(r1: str, r2: str, r3: str) -> int:
    r1_un, r2_un, r3_un = set(r1), set(r2), set(r3)
    rep_items = r1_un.intersection(r2_un).intersection(r3_un)
    return prio[rep_items.pop()]


res = 0
i = 0
while i < len(data):
    res += rep_item_prio(*data[i:i+3])
    i += 3

print(res)
