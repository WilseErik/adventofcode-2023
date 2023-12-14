""" Solution to part one of day 14 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 14
CORRECT_EXAMPLE_ANSWER = 136


def weight_of_grid(grid):
    return sum([row.count('O')*(len(grid)-index)
                for index, row in enumerate(grid)])


def tilt_north(grid):
    done = False
    while not done:
        done = True
        for r in range(len(grid)-1):
            for c in range(len(grid[0])):
                if grid[r][c] == '.' and grid[r+1][c] == 'O':
                    grid[r][c] = 'O'
                    grid[r+1][c] = '.'
                    done = False
    return grid


def solve(input_lines):
    grid = [[c for c in row] for row in input_lines]
    grid = tilt_north(grid)
    return weight_of_grid(grid)

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
