robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
resources = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
costs = {'ore': 4, 'clay': 2, 'obsidian': (3, 14), 'geode': (2, 7)}


def mining(robots, resources, time):
    if time == 0:
        return resources['geode']
    else:
        no_out, ore_out, cla_out, obs_out, geo_out = 0, 0, 0, 0, 0
        if resources['ore'] - costs['geode'][0] >= 0 and resources['obsidian'] - costs['geode'][1] >= 0:
            geode_robots = robots.copy()
            geode_resources = {key: robots[key] + resources[key] for key in robots}
            geode_robots['geode'] += 1
            geode_resources['ore'] -= costs['geode'][0]
            geode_resources['obsidian'] -= costs['geode'][1]
            geo_out = mining(geode_robots, geode_resources, time - 1)
        if resources['ore'] - costs['obsidian'][0] >= 0 and resources['clay'] - costs['obsidian'][1] >= 0:
            obsidian_robots = robots.copy()
            obsidian_resources = {key: robots[key] + resources[key] for key in robots}
            obsidian_robots['obsidian'] += 1
            obsidian_resources['ore'] -= costs['obsidian'][0]
            obsidian_resources['clay'] -= costs['obsidian'][1]
            obs_out = mining(obsidian_robots, obsidian_resources, time - 1)
        if resources['ore'] - costs['clay'] >= 0:
            clay_robots = robots.copy()
            clay_resources = {key: robots[key] + resources[key] for key in robots}
            clay_robots['clay'] += 1
            clay_resources['ore'] -= costs['clay']
            cla_out = mining(clay_robots, clay_resources, time - 1)
        if resources['ore'] - costs['ore'] >= 0:
            ore_robots = robots.copy()
            ore_resources = {key: robots[key] + resources[key] for key in robots}
            ore_robots['ore'] += 1
            ore_resources['ore'] -= costs['ore']
            ore_out = mining(ore_robots, ore_resources, time - 1)
        no_robots = robots.copy()
        no_resources = {key: robots[key] + resources[key] for key in robots}
        no_out = mining(no_robots, no_resources, time - 1)
        return max(no_out, ore_out, cla_out, obs_out, geo_out)


print(mining(robots, resources, 20))