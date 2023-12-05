""" Solution to part two of day 5 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 5
CORRECT_EXAMPLE_ANSWER = 46


class FarmMap:
    """ Maps one farming variable to another """

    def __init__(self, lines):
        self.lines = [s for s in lines]
        self.ranges = []
        for line in lines[1:]:
            items = [int(x) for x in line.split()]
            self.ranges.append({'dst':items[0], 'src':items[1], 'len':items[2]})

    def conv(self, value):
        result = value
        for r in self.ranges:
            if (r['src'] <= value) and (value < r['src']+r['len']):
                return r['dst'] + (value - r['src'])
        return result

    def back_conv(self, value):
        result = value
        for r in self.ranges:
            if (r['dst'] <= value) and (value < r['dst']+r['len']):
                return r['src'] + (value - r['dst'])
        return result


def parse_input(lines):
    map_lines = []
    maps = []
    for line in lines:
        line = line.strip()
        if 'seeds:' in line:
            items = [int(s) for s in line.split()[1:]]
            seeds = [{'start':items[i], 'len':items[i+1]}
                     for i in range(0, len(items), 2)]
        else:
            if len(line) != 0:
                map_lines.append(line)
            elif len(map_lines) != 0:
                maps.append(FarmMap(map_lines))
                map_lines = []
    maps.append(FarmMap(map_lines))
    return seeds, maps


def calc_min_loc_of_points(points, maps):
    min_loc = 10000000000
    for s in points:
        for map_ in maps:
            s = map_.conv(s)
        if s <= min_loc:
            min_loc = s
    return min_loc


def solve(input_lines):
    seeds, maps = parse_input(input_lines)
    points = []
    margin = 2
    # Add all limit values from the seeds
    for s in seeds:
        points += [s['start']+i for i in range(-margin,margin,1)]
        points += [s['start']+s['len']+i for i in range(-margin,margin,1)]
    new_points = []
    # Propagate to location values
    for p in points:
        for map_ in maps:
            p = map_.conv(p)
        new_points.append(p)
    points = [x for x in new_points]
    # Add all range limit values from the maps and backpropagate to inital seed
    # values
    for i in range(len(maps)-1, -1, -1):
        points = [maps[i].back_conv(x) for x in points]
        for r in maps[i].ranges:
            points += [r['src']+i for i in range(-margin,margin,1)]
            points += [r['src']+r['len']+i for i in range(-margin,margin,1)]
    # Remove any values that does not belong to a seed
    valid_seed_points = []
    for p in points:
        valid = False
        for s in seeds:
            if not valid and s['start'] <= p and p < (s['start']+s['len']):
                valid_seed_points.append(p)
                valid = True
    # Calculate minimum location
    min_loc = calc_min_loc_of_points(valid_seed_points, maps)
    return min_loc


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
