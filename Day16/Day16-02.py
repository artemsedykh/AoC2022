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


def add_pressure(nzvo):
    acc = 0
    for v in nzvo:
        acc += valves[v]['flow']
    return acc


def opt_press_m(mdir, edir, mmov, emov, time, press, nzvo, nzvc):
    if mmov > 0:
        return opt_press_e(mdir, edir, mmov - 1, emov, time, press, nzvo, nzvc)
    else:
        nzvo_edit = nzvo.copy()
        if mdir != 'AA':
            nzvo_edit.add(mdir)
        if nzvc:
            max_val = 0
            for v in nzvc:
                nzvc_edit = nzvc.copy()
                nzvc_edit.remove(v)
                max_val = max(max_val, opt_press_e(v, edir, len(min_tracks[mdir][v]) - 1, emov,
                                                   time, press, nzvo_edit, nzvc_edit))
            return max_val
        else:
            return opt_press_e(mdir, edir, mmov - 1, emov, time, press, nzvo_edit, nzvc)


def opt_press_e(mdir, edir, mmov, emov, time, press, nzvo, nzvc):
    # print(mdir, edir, str(mmov).rjust(3), str(emov).rjust(3), str(26-time).rjust(2), str(press).rjust(4), nzvo, nzvc)
    if time > 0:
        if emov > 0:
            if mmov > 0:
                delta = min(emov, mmov, time)
                return opt_press_m(mdir, edir, mmov - delta + 1, emov - delta, time - delta,
                                   press + add_pressure(nzvo) * delta, nzvo, nzvc)
            else:
                return opt_press_m(mdir, edir, mmov, emov - 1, time - 1, press + add_pressure(nzvo), nzvo, nzvc)
        else:
            nzvo_edit = nzvo.copy()
            if edir != 'AA':
                nzvo_edit.add(edir)
            if nzvc:
                max_val = 0
                for v in nzvc:
                    nzvc_edit = nzvc.copy()
                    nzvc_edit.remove(v)
                    max_val = max(max_val, opt_press_m(mdir, v, mmov, len(min_tracks[edir][v]) - 1,
                                                       time - 1, press + add_pressure(nzvo_edit), nzvo_edit, nzvc_edit))
                return max_val
            else:
                if mmov > 0:
                    return opt_press_m(mdir, edir, mmov, emov - 1, time - 1,
                                       press + add_pressure(nzvo_edit), nzvo_edit, nzvc)
                else:
                    return opt_press_m(mdir, edir, mmov, emov - 1, 0,
                                       press + add_pressure(nzvo_edit) * time, nzvo_edit, nzvc)
    else:
        return press


print(opt_press_m('AA', 'AA', 0, 0, 26, 0, nz_valves_open, nz_valves_close))
