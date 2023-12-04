""" Solution to part two of day 3 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import aocd
import colorama

CURRENT_DAY = 3
CORRECT_EXAMPLE_ANSWER = 467835

def is_gear_symbol(c):
    return c=='*'


def length_of_part_number(schematic, row, col):
    idx = 0
    while col+idx < len(schematic[row]) and schematic[row][col+idx].isdigit():
        idx += 1
    return idx


def is_within_bounds(schematic, row, col):
    return (
        (row >= 0) and
        (col >= 0) and
        (row < len(schematic)) and
        (col < len(schematic[0])))


def get_number(schematic, row, col):
    start_idx = col
    end_idx = col
    while start_idx >= 0 and schematic[row][start_idx].isdigit():
        start_idx -= 1
    if not schematic[row][start_idx].isdigit():
        start_idx += 1
    while end_idx < len(schematic[row]) and schematic[row][end_idx].isdigit():
        end_idx += 1
    return int(schematic[row][start_idx:end_idx])


def get_adjecent_numbers(schematic, row, col):
    numbers = []
    if is_within_bounds(schematic, row, col-1) and \
       schematic[row][col-1].isdigit():
        numbers.append(get_number(schematic, row, col-1))
    if is_within_bounds(schematic, row, col+1) and \
       schematic[row][col+1].isdigit():
        numbers.append(get_number(schematic, row, col+1))
    if is_within_bounds(schematic, row-1, col) and \
       schematic[row-1][col].isdigit():
        numbers.append(get_number(schematic, row-1, col))
    else:
        if is_within_bounds(schematic, row-1, col-1) and \
           schematic[row-1][col-1].isdigit():
            numbers.append(get_number(schematic, row-1, col-1))
        if is_within_bounds(schematic, row-1, col+1) and \
           schematic[row-1][col+1].isdigit():
            numbers.append(get_number(schematic, row-1, col+1))
    if is_within_bounds(schematic, row+1, col) and \
       schematic[row+1][col].isdigit():
        numbers.append(get_number(schematic, row+1, col))
    else:
        if is_within_bounds(schematic, row+1, col-1) and \
           schematic[row+1][col-1].isdigit():
            numbers.append(get_number(schematic, row+1, col-1))
        if is_within_bounds(schematic, row+1, col+1) and \
           schematic[row+1][col+1].isdigit():
            numbers.append(get_number(schematic, row+1, col+1))
    return numbers


def solve(input_lines):
    gear_ratios = []
    for r, row in enumerate(input_lines):
        for c, col in enumerate(row.strip()):
            if is_gear_symbol(col):
                adjecent_numbers = get_adjecent_numbers(input_lines, r, c)
                if len(adjecent_numbers)==2:
                    gear_ratios.append(adjecent_numbers[0]*adjecent_numbers[1])
                    print(colorama.Fore.GREEN + input_lines[r][c], end='')
                else:
                    print(colorama.Fore.RED + input_lines[r][c], end='')
            else:
                print(colorama.Fore.WHITE + input_lines[r][c], end='')
        print('')
    print(colorama.Style.RESET_ALL)
    return sum(gear_ratios)


if __name__ == '__main__':
    colorama.init()
    with open('test_input_part_two.txt', 'r') as f:
        example_input_lines = f.readlines()
    example_answer = solve([s.strip() for s in example_input_lines])
    print(f'Example answer = {example_answer}')
    assert example_answer == CORRECT_EXAMPLE_ANSWER
    puzzle_input_lines = aocd.get_data(day=CURRENT_DAY, year=2023).split('\n')
    print('Puzzle answer = {:}'.format(solve(puzzle_input_lines)))
