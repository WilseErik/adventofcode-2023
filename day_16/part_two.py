""" Solution to part two of day 16 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 16
CORRECT_EXAMPLE_ANSWER = 51

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
    count = []
    last_col = len(grid[0])-1
    last_row = len(grid)-1
    for r in range(len(grid)):
        count.append(count_energized_cells(grid, r, 0, RIGHT))
        count.append(count_energized_cells(grid, r, last_col, LEFT))
    for c in range(len(grid[0])):
        count.append(count_energized_cells(grid, 0, c, DOWN))
        count.append(count_energized_cells(grid, last_row, c, UP))
    return max(count)


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
