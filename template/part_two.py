""" Solution to part two of day X of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import aocd

CURRENT_DAY = 1
CORRECT_EXAMPLE_ANSWER = 0

def solve(input_lines):
    return 0

if __name__ == '__main__':
    with open('test_input_part_two.txt', 'r') as f:
        example_input_lines = f.readlines()
    example_answer = solve(example_input_lines)
    print(f'Example answer = {example_answer}')
    assert example_answer == CORRECT_EXAMPLE_ANSWER
    puzzle_input_lines = aocd.get_data(day=CURRENT_DAY, year=2023).split('\n')
    print('Puzzle answer = {:}'.format(solve(puzzle_input_lines)))
