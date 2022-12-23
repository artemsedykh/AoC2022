import datetime
import functools

ore_rob, cla_rob, obs_rob, geo_rob = 1, 0, 0, 0
ore_res, cla_res, obs_res, geo_res = 0, 0, 0, 0
ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst = 4, 2, 3, 14, 2, 7


@functools.cache
def mining(ore_rob, cla_rob, obs_rob, geo_rob, ore_res, cla_res, obs_res, geo_res, ore_ore_cst,
           cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst, time):
    if time == 0:
        return geo_res
    else:
        no_out, ore_out, cla_out, obs_out, geo_out = 0, 0, 0, 0, 0
        if ore_res >= geo_ore_cst and obs_res >= geo_obs_cst:
            geo_out = mining(ore_rob, cla_rob, obs_rob, geo_rob + 1,
                             ore_res + ore_rob - geo_ore_cst, cla_res + cla_rob, obs_res + obs_rob - geo_obs_cst,
                             geo_res + geo_rob,
                             ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst, time - 1)
        if ore_res >= obs_ore_cst and cla_res >= obs_cla_cst:
            obs_out = mining(ore_rob, cla_rob, obs_rob + 1, geo_rob,
                             ore_res + ore_rob - obs_ore_cst, cla_res + cla_rob - obs_cla_cst, obs_res + obs_rob,
                             geo_res + geo_rob,
                             ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst, time - 1)
        if ore_res >= cla_ore_cst:
            cla_out = mining(ore_rob, cla_rob + 1, obs_rob, geo_rob,
                             ore_res + ore_rob - cla_ore_cst, cla_res + cla_rob, obs_res + obs_rob, geo_res + geo_rob,
                             ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst, time - 1)
        if ore_res >= ore_ore_cst:
            ore_out = mining(ore_rob + 1, cla_rob, obs_rob, geo_rob,
                             ore_res + ore_rob - ore_ore_cst, cla_res + cla_rob, obs_res + obs_rob, geo_res + geo_rob,
                             ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst, time - 1)
        no_out = mining(ore_rob, cla_rob, obs_rob, geo_rob,
                        ore_res + ore_rob, cla_res + cla_rob, obs_res + obs_rob, geo_res + geo_rob,
                        ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst, time - 1)
        return max(no_out, ore_out, cla_out, obs_out, geo_out)


with open('day19.txt', 'r') as file:
    line = file.readline()
    i = 0
    while line and i < 3:
        ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst = [int(s) for s in line.split() if
                                                                                        s.strip().isdigit()]
        start = datetime.datetime.now()
        print(i, start)
        print(mining(ore_rob, cla_rob, obs_rob, geo_rob, ore_res, cla_res, obs_res, geo_res,
                     ore_ore_cst, cla_ore_cst, obs_ore_cst, obs_cla_cst, geo_ore_cst, geo_obs_cst, 32))
        end = datetime.datetime.now()
        print(end - start)
        line = file.readline()
        i += 1


