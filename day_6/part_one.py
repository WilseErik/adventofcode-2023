""" Solution to part one of day 6 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
import numpy as np
import math
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 6
CORRECT_EXAMPLE_ANSWER = 288


def calc_num_solutions(time, distance):
    roots = np.roots([1, -time, distance])
    a, b = int(math.ceil(min(roots))), int(math.floor(max(roots)))
    count = b-a+1
    if time*a-a*a == distance:
        count = count - 1
    if time*b-b*b == distance:
        count = count - 1
    return count


def solve(input_lines):
    times = [int(x) for x in input_lines[0].split()[1:]]
    distances = [int(x) for x in input_lines[1].split()[1:]]
    solutions = [calc_num_solutions(t, s) for t, s in zip(times, distances)]
    return np.prod(solutions)


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
