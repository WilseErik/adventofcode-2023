""" Solution to part one of day 1 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import aocd

CURRENT_DAY = 1
CORRECT_EXAMPLE_ANSWER = 142

def solve(in_lines):
    all_digits = [[s for s in line if s.isdigit()] for line in in_lines]
    cal_value = sum([int(row[0]+row[-1]) for row in all_digits])
    return cal_value

if __name__ == '__main__':
    with open('test_input_part_one.txt', 'r') as f:
        example_input_lines = f.readlines()
    example_answer = solve(example_input_lines)
    print(f'Example answer = {example_answer}')
    assert example_answer == CORRECT_EXAMPLE_ANSWER
    input_lines = aocd.get_data(day=CURRENT_DAY, year=2023).split('\n')
    print('Puzzle answer = {:}'.format(solve(input_lines)))
