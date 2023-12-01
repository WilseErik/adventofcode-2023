""" Solution to part two of day 1 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import aocd

CURRENT_DAY = 1
CORRECT_EXAMPLE_ANSWER = 281

def replace_digits(s):
    digits_dict = {
        'one':'1', 'two':'2', 'three':'3',
        'four':'4', 'five':'5','six':'6',
        'seven':'7', 'eight':'8', 'nine':'9'}
    for key, value in digits_dict.items():
        s = s.replace(key, key[0]+value+key[-1])
    return s

def solve(input_lines):
    all_lines = [replace_digits(line) for line in input_lines]
    all_digits = [[s for s in line if s.isdigit()] for line in all_lines]
    cal_value = sum([int(row[0]+row[-1]) for row in all_digits])
    return cal_value


if __name__ == '__main__':
    with open('test_input_part_two.txt', 'r') as f:
        example_input_lines = f.readlines()
    example_answer = solve(example_input_lines)
    print('Example answer = {:}'.format(example_answer))
    assert example_answer == CORRECT_EXAMPLE_ANSWER
    input_lines = aocd.get_data(day=CURRENT_DAY, year=2023).split('\n')
    print('Puzzle answer = {:}'.format(solve(input_lines)))
