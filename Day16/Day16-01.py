valves = dict()

with open('day16.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        parsed = line.replace('Valve ', '').replace('has flow rate=', '') \
            .replace('; tunnels lead to valves', '').replace('; tunnel leads to valve', '') \
            .replace(',', '').split()
        valves[parsed[0]] = {"flow": int(parsed[1]), "connections": parsed[2:]}
        line = file.readline().strip()

nodes = list(valves.keys())
min_tracks = dict()

for v in valves.keys():
    min_tracks[v] = {k: list(valves.keys()) for k in valves.keys()}
    min_tracks[v][v] = [v]

for v in valves.keys():
    for m in valves[v]['connections']:
        min_tracks[v][m], min_tracks[m][v] = [v, m], [m, v]

for _ in valves.keys():
    for n in nodes:
        for m in nodes:
            if n != m and not m in valves[n]['connections']:
                min_k, min_len = [], len(valves.keys())
                for k in valves[n]['connections']:
                    if min_len > len(min_tracks[k][m]) and k != n:
                        min_len, min_k = len(min_tracks[k][m]), k
                if min_len + 1 < len(min_tracks[n][m]):
                    res = [n] + min_tracks[min_k][m]
                    min_tracks[n][m] = res
                    min_tracks[m][n] = res[::-1]

nz_valves_open = set()
nz_valves_close = set()
for v in valves.keys():
    if valves[v]['flow'] > 0:
        nz_valves_close.add(v)


def add_pressure():
    acc = 0
    for v in nz_valves_open:
        acc += valves[v]['flow']
    return acc


def opt_press(pos, time, total_pressure):
    if time > 0:
        if pos != 'AA':
            nz_valves_open.add(pos)
            nz_valves_close.remove(pos)
        max_val = 0
        if nz_valves_close:
            for v in nz_valves_close:
                av_moves = min(len(min_tracks[pos][v]), time)
                max_val = max(max_val, opt_press(v, time - av_moves, total_pressure + add_pressure() * av_moves))
            if pos != 'AA':
                nz_valves_open.remove(pos)
                nz_valves_close.add(pos)
            return max_val
        else:
            total_pressure += add_pressure() * time
            if pos != 'AA':
                nz_valves_open.remove(pos)
                nz_valves_close.add(pos)
            return total_pressure
    else:
        return total_pressure


print(opt_press('AA', 30, 0))