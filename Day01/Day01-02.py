with open('day01.txt', 'r') as file:
    data = [line.strip() for line in file]


def form_cal_top3(a, b, c, val):
    if val > a:
        return val, a, b
    elif a <= val < b:
        return a, val, b
    elif b <= val < c:
        return a, b, val
    return a, b, c


cal_top3 = [0] * 3
acc = 0
for food in data:
    if food:
        acc += int(food)
    else:
        cal_top3 = form_cal_top3(*cal_top3, acc)
        acc = 0
cal_top3 = form_cal_top3(*cal_top3, acc)
print(sum(cal_top3))
