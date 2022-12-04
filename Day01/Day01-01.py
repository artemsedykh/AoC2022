with open('day01.txt', 'r') as file:
    data = [line.strip() for line in file]

max_cal, acc = 0, 0
for food in data:
    if food:
        acc += int(food)
    else:
        max_cal = max(max_cal, acc)
        acc = 0
max_cal = max(max_cal, acc)
print(max_cal)
