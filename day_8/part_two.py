""" Solution to part two of day 8 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
import math
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 8
CORRECT_EXAMPLE_ANSWER = 6

def get_cycle(nodes, n, sequence):
    i = 0
    while n[-1] != 'Z':
        n = nodes[n][sequence[i%len(sequence)]=='R']
        i = i + 1
    return i


def solve(input_lines):
    sequence = input_lines[0].strip()
    nodes = {}
    for line in input_lines[2:]:
        items = line.replace('(', '').replace(')', '').replace(',', '').split()
        nodes[items[0]] = (items[2],items[3])
    start_nodes = [x for x in nodes if x[-1]=='A']
    cycles = [get_cycle(nodes, n, sequence) for n in start_nodes]
    return math.lcm(*cycles)

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
