ore_rob, cla_rob, obs_rob, geo_rob = 1, 0, 0, 0
ore_res, cla_res, obs_res, geo_res = 0, 0, 0, 0
ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst = 4, 2, 3, 14, 2, 7


def mining(ore_rob, cla_rob, obs_rob, geo_rob, ore_res, cla_res, obs_res, geo_res, ore_ore_cst,
           cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst, time):
    if time == 0:
        return geo_res
    elif time == 1:
        return geo_res + geo_rob
    else:
        no_out, ore_out, cla_out, obs_out, geo_out = 0, 0, 0, 0, 0
        # decision: make ore_rob
        if ore_rob < max(ore_ore_cst, cla_ore_cst, obs_ore_cst, geo_ore_cst):
            temp_ore_res, temp_cla_res, temp_obs_res, temp_geo_res, t = ore_res, cla_res, obs_res, geo_res, 0
            while temp_ore_res < ore_ore_cst:
                temp_ore_res += ore_rob
                temp_cla_res += cla_rob
                temp_obs_res += obs_rob
                temp_geo_res += geo_rob
                t += 1
            if t < time:
                temp_ore_res += (ore_rob - ore_ore_cst)
                temp_cla_res += cla_rob
                temp_obs_res += obs_rob
                temp_geo_res += geo_rob
                ore_out = mining(ore_rob + 1, cla_rob, obs_rob, geo_rob, temp_ore_res, temp_cla_res, temp_obs_res,
                                 temp_geo_res, ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst,
                                 geo_obs_cst, time - t - 1)
        # decision: make cla_rob
        temp_ore_res, temp_cla_res, temp_obs_res, temp_geo_res, t = ore_res, cla_res, obs_res, geo_res, 0
        while temp_ore_res < cla_ore_cst:
            temp_ore_res += ore_rob
            temp_cla_res += cla_rob
            temp_obs_res += obs_rob
            temp_geo_res += geo_rob
            t += 1
        if t < time:
            temp_ore_res += (ore_rob - cla_ore_cst)
            temp_cla_res += cla_rob
            temp_obs_res += obs_rob
            temp_geo_res += geo_rob
            cla_out = mining(ore_rob, cla_rob + 1, obs_rob, geo_rob, temp_ore_res, temp_cla_res, temp_obs_res,
                             temp_geo_res, ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst,
                             geo_obs_cst, time - t - 1)
        # decision: make obs_rob
        if cla_rob > 0:
            temp_ore_res, temp_cla_res, temp_obs_res, temp_geo_res, t = ore_res, cla_res, obs_res, geo_res, 0
            while temp_ore_res < obs_ore_cst or temp_cla_res < obs_cla_cst:
                temp_ore_res += ore_rob
                temp_cla_res += cla_rob
                temp_obs_res += obs_rob
                temp_geo_res += geo_rob
                t += 1
            if t < time:
                temp_ore_res += (ore_rob - obs_ore_cst)
                temp_cla_res += (cla_rob - obs_cla_cst)
                temp_obs_res += obs_rob
                temp_geo_res += geo_rob
                obs_out = mining(ore_rob, cla_rob, obs_rob + 1, geo_rob, temp_ore_res, temp_cla_res, temp_obs_res,
                                 temp_geo_res, ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst,
                                 geo_obs_cst, time - t - 1)
        # decision: make geo_rob
        if obs_rob > 0:
            temp_ore_res, temp_cla_res, temp_obs_res, temp_geo_res, t = ore_res, cla_res, obs_res, geo_res, 0
            while temp_ore_res < geo_ore_cst or temp_obs_res < geo_obs_cst:
                temp_ore_res += ore_rob
                temp_cla_res += cla_rob
                temp_obs_res += obs_rob
                temp_geo_res += geo_rob
                t += 1
            if t < time:
                temp_ore_res += (ore_rob - geo_ore_cst)
                temp_cla_res += cla_rob
                temp_obs_res += (obs_rob - geo_obs_cst)
                temp_geo_res += geo_rob
                geo_out = mining(ore_rob, cla_rob, obs_rob, geo_rob + 1, temp_ore_res, temp_cla_res, temp_obs_res,
                                 temp_geo_res, ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst,
                                 geo_obs_cst, time - t - 1)
        if ore_out == cla_out == obs_out == geo_out == 0:
            temp_ore_res, temp_cla_res, temp_obs_res, temp_geo_res, t = ore_res, cla_res, obs_res, geo_res, 0
            while t < time:
                temp_ore_res += ore_rob
                temp_cla_res += cla_rob
                temp_obs_res += obs_rob
                temp_geo_res += geo_rob
                t += 1
            no_out = temp_geo_res
        return max(no_out, ore_out, cla_out, obs_out, geo_out)


with open('day19.txt', 'r') as file:
    line = file.readline()
    i = 1
    acc = 1
    while line and i <= 3:
        ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst = [int(s) for s in line.split() if
                                                                                        s.strip().isdigit()]
        acc *= mining(ore_rob, cla_rob, obs_rob, geo_rob, ore_res, cla_res, obs_res, geo_res,
                        ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst, 32)
        line = file.readline()
        i += 1

print(acc)