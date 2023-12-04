""" Solution to part one of day 4 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import aocd

CURRENT_DAY = 4
CORRECT_EXAMPLE_ANSWER = 13

def solve(input_lines):
    total_points = 0
    for line in input_lines:
        fields = line.replace(':', '|').split('|')
        winning_numbers = [int(x) for x in fields[1].split()]
        own_numbers = [int(x) for x in fields[2].split()]
        intersection = list(set(winning_numbers).intersection(own_numbers))
        if len(intersection) != 0:
            points = 2**(len(intersection)-1)
            total_points += points
    return total_points

if __name__ == '__main__':
    with open('test_input_part_one.txt', 'r') as f:
        example_input_lines = f.readlines()
    example_answer = solve([x.strip() for x in example_input_lines])
    print(f'Example answer = {example_answer}')
    assert example_answer == CORRECT_EXAMPLE_ANSWER
    puzzle_input_lines = aocd.get_data(day=CURRENT_DAY, year=2023).split('\n')
    print('Puzzle answer = {:}'.format(solve(puzzle_input_lines)))
