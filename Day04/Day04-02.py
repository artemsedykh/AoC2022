with open('day04.txt', 'r') as file:
    data = file.read().split()


def does_overlap(sections: str) -> bool:
    section1, section2 = sections.split(',')
    l1, r1 = map(int, section1.split('-'))
    l2, r2 = map(int, section2.split('-'))
    return l2 <= l1 <= r2 or l2 <= r1 <= r2 \
        or l1 <= l2 <= r1 or l1 <= r2 <= r1


count = 0
for sections in data:
    if does_overlap(sections):
        count += 1
print(count)
