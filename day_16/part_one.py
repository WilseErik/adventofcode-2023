""" Solution to part one of day 16 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 16
CORRECT_EXAMPLE_ANSWER = 46

UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4


def grid_index_is_valid(grid, row, col):
    return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))


def count_energized_cells(grid, start_row, start_col, start_direction):
    dir_dict = {UP:(-1, 0), RIGHT:(0, 1), DOWN:(1, 0), LEFT:(0, -1)}
    visited = set()
    energized_cells = set()
    rays = [(start_row, start_col, start_direction)]
    while len(rays) != 0:
        row, col, direction = rays.pop()
        if (row, col, direction) in visited:
            continue
        visited.add((row, col, direction))
        energized_cells.add((row, col))
        if ((grid[row][col] in '\\/.')
            or (grid[row][col]=='|' and (direction==UP or direction==DOWN))
            or (grid[row][col]=='-' and (direction==LEFT or direction==RIGHT))):
            if grid[row][col] == '\\':
                direction = {UP:LEFT, RIGHT:DOWN, DOWN:RIGHT, LEFT:UP}[direction]
            elif grid[row][col] == '/':
                direction = {UP:RIGHT, RIGHT:UP, DOWN:LEFT, LEFT:DOWN}[direction]
            dr, dc = dir_dict[direction]
            if grid_index_is_valid(grid, row+dr, col+dc):
                rays.append((row+dr, col+dc, direction))
        elif grid[row][col] == '|':
            dr, dc = dir_dict[UP]
            if grid_index_is_valid(grid, row+dr, col+dc):
                rays.append((row+dr, col+dc, UP))
            dr, dc = dir_dict[DOWN]
            if grid_index_is_valid(grid, row+dr, col+dc):
                rays.append((row+dr, col+dc, DOWN))
        elif grid[row][col] == '-':
            dr, dc = dir_dict[LEFT]
            if grid_index_is_valid(grid, row+dr, col+dc):
                rays.append((row+dr, col+dc, LEFT))
            dr, dc = dir_dict[RIGHT]
            if grid_index_is_valid(grid, row+dr, col+dc):
                rays.append((row+dr, col+dc, RIGHT))
    return len(energized_cells)



def solve(input_lines):
    visited = set()
    grid = [list(row) for row in input_lines]
    return count_energized_cells(grid, 0, 0, RIGHT)


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
