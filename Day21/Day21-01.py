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

print(int(find_num('root')))
