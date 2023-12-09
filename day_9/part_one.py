""" Solution to part one of day 9 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 9
CORRECT_EXAMPLE_ANSWER = 114

def extrapolate_sequence(s):
    diff = []
    while s != [0]*len(s):
        diff.append(s)
        s = [s[i+1]-s[i] for i in range(len(s)-1)]
    diff.append(s)
    diff.reverse()
    for i in range(len(diff)-1):
        diff[i+1].append(diff[i+1][-1]+diff[i][-1])
    return diff[-1][-1]


def solve(input_lines):
    sequences = [[int(x) for x in line.split()] for line in input_lines]
    next_vals = [extrapolate_sequence(seq) for seq in sequences]
    return sum(next_vals)

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
