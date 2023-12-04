""" Solution to part one of day 2 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import aocd

CURRENT_DAY = 2
CORRECT_EXAMPLE_ANSWER = 8

def parse_game(line):
    game = {'id':int(line.split()[1][:-1]), 'red':0, 'green':0, 'blue':0}
    for game_round in line.strip().split(':')[1].split(';'):
        game_round = game_round.replace(',', '')
        fields = game_round.split()
        for i in range(0, len(fields), 2):
            game[fields[i+1]] = max(game[fields[i+1]], int(fields[i]))
    return game


def game_is_possible(game):
    return (
        (game['red'] <= 12) and
        (game['green'] <= 13) and
        (game['blue'] <= 14))


def solve(input_lines):
    games = list(map(parse_game, input_lines))
    return sum([x['id'] for x in games if game_is_possible(x)])


if __name__ == '__main__':
    with open('test_input_part_one.txt', 'r') as f:
        example_input_lines = f.readlines()
    example_answer = solve(example_input_lines)
    print(f'Example answer = {example_answer}')
    assert example_answer == CORRECT_EXAMPLE_ANSWER
    puzzle_input_lines = aocd.get_data(day=CURRENT_DAY, year=2023).split('\n')
    print('Puzzle answer = {:}'.format(solve(puzzle_input_lines)))
