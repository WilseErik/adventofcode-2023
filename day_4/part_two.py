""" Solution to part two of day 4 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import aocd

CURRENT_DAY = 4
CORRECT_EXAMPLE_ANSWER = 30

def calc_number_of_matches(card_line):
    fields = card_line.replace(':', '|').split('|')
    winning_numbers = [int(x) for x in fields[1].split()]
    own_numbers = [int(x) for x in fields[2].split()]
    intersection = list(set(winning_numbers).intersection(own_numbers))
    return len(intersection)


def solve(input_lines):
    card_matches = [calc_number_of_matches(line) for line in input_lines]
    card_count_list = [1 for line in input_lines]
    for card_id, card_count in enumerate(card_count_list):
        for i in range(card_matches[card_id]):
            card_count_list[card_id+i+1] += card_count
    return sum(card_count_list)


if __name__ == '__main__':
    with open('test_input_part_two.txt', 'r') as f:
        example_input_lines = f.readlines()
    example_answer = solve(example_input_lines)
    print(f'Example answer = {example_answer}')
    assert example_answer == CORRECT_EXAMPLE_ANSWER
    puzzle_input_lines = aocd.get_data(day=CURRENT_DAY, year=2023).split('\n')
    print('Puzzle answer = {:}'.format(solve(puzzle_input_lines)))
