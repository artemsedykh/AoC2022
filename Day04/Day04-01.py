with open('day04.txt', 'r') as file:
    data = file.read().split()


def does_fully_contain(sections: str) -> bool:
    section1, section2 = sections.split(',')
    l1, r1 = map(int, section1.split('-'))
    l2, r2 = map(int, section2.split('-'))
    return (l2 <= l1 and r1 <= r2) or (l1 <= l2 and r2 <= r1)


count = 0
for sections in data:
    if does_fully_contain(sections):
        count += 1
print(count)
