with open('day11.txt', 'r') as file:
    monkeys = []
    line = file.readline().strip()
    while line:
        items = file.readline().strip()
        oper = file.readline().strip()
        test = file.readline().strip()
        iftrue = file.readline().strip()
        iffalse = file.readline().strip()
        monkeys.append({
            "items": [int(i) for i in items.split(':')[1].split(',')],
            "oper": oper.split(':')[1].strip(),
            "test": int(test.split()[-1]),
            "t": int(iftrue.split()[-1]),
            "f": int(iffalse.split()[-1]),
            "insp": 0
        })
        line = file.readline().strip()
        line = file.readline().strip()

def new_level(item, oper):
    new_item = item
    ari, arg = oper.split()[-2:]
    if ari == '+':
        if arg == 'old':
            new_item += item
        else:
            new_item += int(arg)
    elif ari == '*':
        if arg == 'old':
            new_item *= item
        else:
            new_item *= int(arg)
    return new_item

div = 1
for monkey in monkeys:
    div *= monkey['test']

rnd = 0
while rnd < 10_000:
    for monkey in monkeys:
        for item in monkey['items']:
            new_item = new_level(item, monkey['oper']) % div
            if new_item % monkey['test'] == 0:
                monkeys[monkey['t']]['items'].append(new_item)
            else:
                monkeys[monkey['f']]['items'].append(new_item)
            monkey['insp'] += 1
        monkey['items'] = []
    rnd += 1

max1, max2 = 0, 0
for monkey in monkeys:
    if monkey['insp'] > max1:
        max1, max2 = monkey['insp'], max1
    elif monkey['insp'] > max2:
        max2 = monkey['insp']

print(max1 * max2)