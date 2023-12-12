""" Solution to part one of day 11 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 11
CORRECT_EXAMPLE_ANSWER = 374

def create_space(input_lines):
    space = [x for x in input_lines]
    row_is_empty = []
    col_is_empty = []
    for row in range(len(space)):
        if '#' not in space[row]:
            row_is_empty.append(1)
        else:
            row_is_empty.append(0)
    for col in range(len(space[0])):
        column = []
        for row in range(len(space)):
            column.append(space[row][col])
        if '#' not in column:
            col_is_empty.append(1)
        else:
            col_is_empty.append(0)
    return space, row_is_empty, col_is_empty


def get_distance(a, b, row_is_empty, col_is_empty):
    r0 = min(a[0], b[0])
    r1 = max(a[0], b[0])
    c0 = min(a[1], b[1])
    c1 = max(a[1], b[1])
    expansion_factor = 2
    r_expansion = sum(row_is_empty[r0:r1])*(expansion_factor-1)
    c_expansion = sum(col_is_empty[c0:c1])*(expansion_factor-1)
    return r1-r0 + c1-c0 + r_expansion + c_expansion


def solve(input_lines):
    space, row_is_empty, col_is_empty = create_space(input_lines)
    galaxies = []
    for row in range(len(space)):
        for col in range(len(space[0])):
            if space[row][col] == '#':
                galaxies.append((row, col))
    dist = 0
    for i in range(len(galaxies)-1):
        for k in range(i+1, len(galaxies)):
            dist += get_distance(
                galaxies[i], galaxies[k], row_is_empty, col_is_empty)
    return dist

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
