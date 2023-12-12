""" Solution to part two of day 10 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
import numpy as np
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 10
CORRECT_EXAMPLE_ANSWER = 10

U, D, R, L = (0, -1), (0, 1), (1, 0), (-1, 0)
neighbour_dict = {
    '|':[U, D], '-':[L, R],  'L':[U, R], 'J':[U, L], '7':[L, D], 'F':[R, D]
}


def count_contained(grid, status):
    y_lim, x_lim = status.shape
    count = 0
    for x in range(x_lim):
        contained = False
        for y in range(y_lim):
            if x+y < x_lim:
                token = grid[y,x+y]
                if status[y, x+y] == 1 and token not in 'L7':
                    contained = not contained
                if status[y, x+y] != 1 and contained:
                    status[y, x+y] = 2
                    count = count + 1
    for y in range(1, y_lim):
        contained = False
        for x in range(x_lim):
            if x+y < y_lim:
                token = grid[x+y,x]
                if status[x+y, x] == 1 and token not in 'L7':
                    contained = not contained
                if status[x+y, x] != 1 and contained:
                    status[x+y, x] = 2
                    count = count + 1
    return count


def get_neighbours(grid, x, y):
    n = neighbour_dict[grid[y, x]]
    return [(x+n[0][0], y+n[0][1]), (x+n[1][0], y+n[1][1])]


def solve(input_lines):
    grid = np.array([[c for c in line.strip()] for line in input_lines])
    status = np.zeros(grid.shape)
    w = np.where(grid=='S')
    start_x, start_y = w[1][0], w[0][0]
    s_direction = []
    if start_y != 0 and grid[start_y-1, start_x] in '|7F':
        x, y = start_x, start_y-1
        s_direction.append(U)
    if start_x != 0 and grid[start_y, start_x-1] in '-LF':
        x, y = start_x-1, start_y
        s_direction.append(L)
    if grid[start_y, start_x+1] in '-7J':
        x, y = start_x+1, start_y
        s_direction.append(R)
    if grid[start_y+1, start_x] in '|LJ':
        x, y = start_x, start_y+1
        s_direction.append(D)
    assert len(s_direction) == 2
    s_token = [t for t, d in neighbour_dict.items() if d == s_direction][0]
    last_x, last_y = start_x, start_y
    status[start_y, start_x] = 1
    while grid[y, x] != 'S':
        status[y, x] = 1
        neigh = get_neighbours(grid, x, y)
        if neigh[0] == (last_x, last_y):
            last_x, last_y = x, y
            x, y = neigh[1]
        else:
            last_x, last_y = x, y
            x, y = neigh[0]
    grid[start_y, start_x] = s_token
    return count_contained(grid, status)


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
