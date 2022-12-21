import copy

monkeys = dict()

with open('day21.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        key, val = line.split(':')
        if val.strip().isdigit():
            monkeys[key] = {"num": int(val)}
        else:
            monkeys[key] = {"monkey1": val[1:5], "oper": val[6:7], "monkey2": val[8:12]}
        line = file.readline().strip()


def find_num(key):
    if 'num' in monkeys[key]:
        return monkeys[key]['num']
    if monkeys[key]['oper'] == '+':
        monkeys[key]['num'] = find_num(monkeys[key]['monkey1']) + find_num(monkeys[key]['monkey2'])
    if monkeys[key]['oper'] == '-':
        monkeys[key]['num'] = find_num(monkeys[key]['monkey1']) - find_num(monkeys[key]['monkey2'])
    if monkeys[key]['oper'] == '*':
        monkeys[key]['num'] = find_num(monkeys[key]['monkey1']) * find_num(monkeys[key]['monkey2'])
    if monkeys[key]['oper'] == '/':
        monkeys[key]['num'] = find_num(monkeys[key]['monkey1']) / find_num(monkeys[key]['monkey2'])
    return monkeys[key]['num']


copy_monkeys = copy.deepcopy(monkeys)
t = find_num('root')
num1, num2 = monkeys[monkeys['root']['monkey1']]['num'], monkeys[monkeys['root']['monkey2']]['num']
humnl, humnr = 0, max(num1, num2)

while num1 != num2:
    monkeys = copy.deepcopy(copy_monkeys)
    monkeys['humn']['num'] = (humnl + humnr) // 2
    t = find_num('root')
    num1, num2 = monkeys[monkeys['root']['monkey1']]['num'], monkeys[monkeys['root']['monkey2']]['num']
    if num1 > num2:
        humnl = (humnl + humnr) // 2
    else:
        humnr = (humnl + humnr) // 2

print(int(monkeys['humn']['num']))


