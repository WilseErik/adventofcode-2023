""" Solution to part one of day 5 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 5
CORRECT_EXAMPLE_ANSWER = 35

class FarmMap:
    """ Maps one farming variable to another """

    def __init__(self, lines):
        self.lines = [s for s in lines]
        self.ranges = []
        for line in lines[1:]:
            items = [int(x) for x in line.split()]
            self.ranges.append({'dst':items[0], 'src':items[1], 'len':items[2]})

    def is_in_src_range(self, range_, value):
        return (range_['src'] <= value) and \
               (value < range_['src']+range_['len'])

    def convert(self, value):
        result = value
        found_range = [r for r in self.ranges if self.is_in_src_range(r, value)]
        if len(found_range) == 1:
            range_ = found_range[0]
            result = range_['dst'] + (value - range_['src'])
        return result


def parse_input(lines):
    map_lines = []
    maps = []
    for line in lines:
        line = line.strip()
        if 'seeds:' in line:
            seeds = [int(s) for s in line.split()[1:]]
        else:
            if len(line) != 0:
                map_lines.append(line)
            elif len(map_lines) != 0:
                maps.append(FarmMap(map_lines))
                map_lines = []
    maps.append(FarmMap(map_lines))
    return seeds, maps


def solve(input_lines):
    seeds, maps = parse_input(input_lines)
    locations = [s for s in seeds]
    for map_ in maps:
        locations = [map_.convert(x) for x in locations]
    return min(locations)


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
