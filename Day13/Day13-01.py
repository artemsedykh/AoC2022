def parse(line):
    stack = []
    for chunk in line:
        if chunk == '[':
            stack.append(chunk)
        elif chunk == '':
            pass
        elif chunk == ']':
            buff = []
            c = stack.pop()
            while c != '[':
                buff.append(c)
                c = stack.pop()
            stack.append(buff[::-1])
        else:
            stack.append(int(chunk))
    return stack


def compare(a, b):
    decision = None
    if type(a) is int:
        if type(b) is int:
            decision = True if a < b else False if a > b else None
        else:
            decision = compare([a], b) if len(b) > 0 else False if len(b) == 0 else None
    else:
        if type(b) is int:
            decision = compare(a, [b]) if len(a) > 0 else True if len(a) == 0 else None
        else:
            i = 0
            while i < min(len(a), len(b)):
                decision = compare(a[i], b[i])
                if decision in (True, False):
                    return decision
                i += 1
            if len(a) <= i < len(b):
                return True
            elif len(b) <= i < len(a):
                return False
    return decision


acc, count = 0, 1
with open('day13.txt', 'r') as file:
    line1 = file.readline().strip()
    line2 = file.readline().strip()
    _ = file.readline().strip()
    while line1:
        split_line1 = line1.replace('[', '[,').replace(']', ',]').split(',')
        split_line2 = line2.replace('[', '[,').replace(']', ',]').split(',')
        acc = acc + count if compare(*parse(split_line1), *parse(split_line2)) else acc
        count += 1
        line1 = file.readline().strip()
        line2 = file.readline().strip()
        _ = file.readline().strip()

print(acc)
