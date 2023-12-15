""" Solution to part one of day 15 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 15
CORRECT_EXAMPLE_ANSWER = 1320

def calc_hash(s):
    value = 0
    for c in s:
        value = ((value+ord(c))*17) % 256
    return value


def solve(input_lines):
    return sum([calc_hash(s) for s in input_lines[0].split(',')])


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
