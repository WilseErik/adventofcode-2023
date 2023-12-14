""" Solution to part two of day 14 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
import numpy as np
import pickle
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 14
CORRECT_EXAMPLE_ANSWER = 64

SPACE = 0
ROCK = 1
WALL = 2

def text_to_grid(lines):
    grid_mapping = {'.':SPACE, 'O':ROCK, '#':WALL}
    return np.array([[grid_mapping[x] for x in line] for line in lines])


def weight_of_grid(grid):
    return sum([np.count_nonzero(row == ROCK)*(len(grid)-index)
                for index, row in enumerate(grid)])


def tilt_north(grid):
    for r in range(grid.shape[1]-1):
        for c in range(grid.shape[0]):
            if grid[r, c] == SPACE and grid[r+1, c] == ROCK:
                new_r = r
                while new_r-1 >= 0 and grid[new_r-1, c] == SPACE:
                    new_r -= 1
                grid[new_r, c] = ROCK
                grid[r+1, c] = SPACE
    return grid


def run_cycle(grid):
    for _ in range(4):
        tilt_north(grid)
        grid = np.rot90(grid, k=-1)


def solve(input_lines):
    grid = text_to_grid(input_lines)
    cycle_offset = 0
    seen = set()
    h = pickle.dumps(grid)
    while not h in seen:
        seen.add(h)
        run_cycle(grid)
        cycle_offset += 1
        h = pickle.dumps(grid)
    #
    cycle_length = 0
    seen = set()
    cycle_weights = []
    h = pickle.dumps(grid)
    while not h in seen:
        cycle_weights.append(weight_of_grid(grid))
        seen.add(h)
        run_cycle(grid)
        h = pickle.dumps(grid)
        cycle_length += 1
    cycle_offset -= cycle_length
    answer = cycle_weights[(1000000000-cycle_offset)%cycle_length]
    return answer


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
