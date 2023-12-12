""" Solution to part one of day 10 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
import numpy as np
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 10
CORRECT_EXAMPLE_ANSWER = 8

U, D, R, L = (0, -1), (0, 1), (1, 0), (-1, 0)

def get_neighbours(grid, x, y):
    neighbour_dict = {
        '|':[U, D], '-':[L, R],  'L':[U, R], 'J':[U, L], '7':[L, D], 'F':[R, D]
    }
    n = neighbour_dict[grid[y, x]]
    return [(x+n[0][0], y+n[0][1]), (x+n[1][0], y+n[1][1])]


def solve(input_lines):
    grid = np.array([[c for c in line.strip()] for line in input_lines])
    w = np.where(grid=='S')
    start_x, start_y = w[1][0], w[0][0]
    if start_y != 0 and grid[start_y-1, start_x] in '|7F':
        x, y = start_x, start_y-1
    elif start_x != 0 and grid[start_y, start_x-1] in '-LF':
        x, y = start_x-1, start_y
    elif grid[start_y+1, start_x] in '|LJ':
        x, y = start_x, start_y+1
    elif grid[start_y, start_x+1] in '-7J':
        x, y = start_x+1, start_y
    else:
        assert False
    step = 1
    last_x, last_y = start_x, start_y
    while grid[y, x] != 'S':
        neigh = get_neighbours(grid, x, y)
        if neigh[0] == (last_x, last_y):
            last_x, last_y = x, y
            x, y = neigh[1]
        else:
            last_x, last_y = x, y
            x, y = neigh[0]
        step = step + 1
    return step/2


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
