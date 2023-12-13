""" Solution to part one of day 13 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
import numpy as np
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 13
CORRECT_EXAMPLE_ANSWER = 405

def parse_mirrors(lines):
    mirrors = []
    m = []
    for line in lines:
        if len(line) == 0:
            mirrors.append(np.array(m))
            m = []
        else:
            m.append([0 if x == '.' else 1 for x in line])
    mirrors.append(np.array(m))
    return mirrors


def is_verticaly_reflected(mirror, row):
    reflected = True
    if row == mirror.shape[0]-1:
        reflected = False
    for r in range(row+1):
        if (row+1+r) < len(mirror) and (mirror[row+1+r]!=mirror[row-r]).any():
            reflected = False
    return reflected


def find_reflection(mirror):
    try:
        refl = 1+[is_verticaly_reflected(mirror, r)
                  for r in range(0, int(len(mirror)))].index(True)
    except:
        refl = -1
    return refl


def solve(input_lines):
    mirrors = parse_mirrors(input_lines)
    return sum([max(100*find_reflection(m), find_reflection(m.T))
                for m in mirrors])


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
