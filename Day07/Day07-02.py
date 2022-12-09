import pprint

fs = {'/': dict()}
curr_dir = fs['/']
path = []

with open('day07.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        args = line.split()
        if args[0] == '$':
            if args[1] == 'cd':
                if args[2] == '/':
                    curr_dir = fs['/']
                    path = []
                elif args[2] == '..':
                    curr_dir = path.pop()
                else:
                    path.append(curr_dir)
                    curr_dir = curr_dir[args[2]]
            elif args[1] == 'ls':
                pass
        elif args[0] == 'dir':
            curr_dir[args[1]] = dict()
        else:
            curr_dir[args[1]] = {'size': int(args[0])}
        line = file.readline().strip()


def dfcount(curr_dir):
    if curr_dir.get('size', -1) == -1:
        acc = 0
        for key in curr_dir.keys():
            acc += dfcount(curr_dir[key])
        curr_dir['size'] = acc
        dirs_size.append(acc)
    return curr_dir['size']

total_size = 70_000_000
req_size = 30_000_000
dirs_size = []
needed_size = req_size - (total_size - dfcount(fs))
dirs_size.sort()
res = list(filter(lambda size: size >= needed_size, dirs_size))[0]
print(needed_size, res)
