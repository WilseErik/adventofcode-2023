""" Solution to part one of day 3 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import aocd
import colorama

CURRENT_DAY = 3
CORRECT_EXAMPLE_ANSWER = 4361

def is_symbol(c):
    return not c.isdigit() and not c=='.'


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


def is_adjecent_to_symbol(schematic, row, col):
    number_len = length_of_part_number(schematic, row, col)
    adjecent = False
    for r in range(3):
        for c in range(number_len+2):
            if is_within_bounds(schematic, row-1+r, col-1+c):
                if is_symbol(schematic[row-1+r][col-1+c]):
                    adjecent = True
    return adjecent


def solve(input_lines):
    part_numbers = []
    for r, row in enumerate(input_lines):
        in_part_number = False
        adjecent = False
        for c, col in enumerate(row.strip()):
            if not in_part_number and col.isdigit():
                in_part_number = True
                if is_adjecent_to_symbol(input_lines, r, c):
                    num_len = length_of_part_number(input_lines, r, c)
                    part_numbers.append(int(input_lines[r][c : c+num_len]))
                    adjecent = True
            if in_part_number and not col.isdigit():
                in_part_number = False
                adjecent = False
            if in_part_number:
                if adjecent:
                    print(colorama.Fore.GREEN + input_lines[r][c], end='')
                else:
                    print(colorama.Fore.RED + input_lines[r][c], end='')
            else:
                print(colorama.Fore.WHITE + input_lines[r][c], end='')
        print('')
    print(colorama.Style.RESET_ALL)
    return sum(part_numbers)


if __name__ == '__main__':
    colorama.init()
    with open('test_input_part_one.txt', 'r') as f:
        example_input_lines = f.readlines()
    example_answer = solve([s.strip() for s in example_input_lines])
    print(f'Example answer = {example_answer}')
    assert example_answer == CORRECT_EXAMPLE_ANSWER
    puzzle_input_lines = aocd.get_data(day=CURRENT_DAY, year=2023).split('\n')
    print('Puzzle answer = {:}'.format(solve(puzzle_input_lines)))
