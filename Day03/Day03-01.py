import string

with open('day03.txt', 'r') as file:
    data = file.read().split()

# set priorities
prio = {}
for c in string.ascii_lowercase:
    prio[c] = ord(c) - ord('a') + 1
for c in string.ascii_uppercase:
    prio[c] = ord(c) - ord('A') + 27


def rep_item_prio(rucksack: str) -> int:
    part_len = len(rucksack) // 2
    part1 = {*rucksack[:part_len]}
    part2 = {*rucksack[part_len:]}
    rep_items = part1.intersection(part2)
    return prio[rep_items.pop()]


res = 0
for rucksack in data:
    res += rep_item_prio(rucksack)

print(res)
