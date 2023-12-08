""" Solution to part one of day 8 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 8
CORRECT_EXAMPLE_ANSWER = 6

def solve(input_lines):
    sequence = input_lines[0].strip()
    nodes = {}
    for line in input_lines[2:]:
        items = line.replace('(', '').replace(')', '').replace(',', '').split()
        nodes[items[0]] = (items[2],items[3])
    i = 0
    n = next(x for x in nodes if x == 'AAA')
    while n != 'ZZZ':
        n = nodes[n][sequence[i%len(sequence)]=='R']
        i = i + 1
    return i

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
