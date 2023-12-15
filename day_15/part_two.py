""" Solution to part two of day 15 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 15
CORRECT_EXAMPLE_ANSWER = 145

def calc_hash(s):
    value = 0
    for c in s:
        value = ((value+ord(c))*17) % 256
    return value


def focusing_power(boxes):
    power = 0
    for i, box in enumerate(boxes):
        for k, lens in enumerate(box):
            power += (i+1)*(k+1)*lens[1]
    return power


def solve(input_lines):
    boxes = [[] for _ in range(256)]
    for instr in input_lines[0].split(','):
        if '=' in instr:
            label, focal_length = instr.split('=')
            box = boxes[calc_hash(label)]
            found = False
            for item in box:
                if item[0]==label:
                    item[1]=int(focal_length)
                    found = True
            if not found:
                box.append([label, int(focal_length)])
        else:
            label = instr[:-1]
            box = boxes[calc_hash(label)]
            for i in reversed(range(len(box))):
                if box[i][0]==label:
                    del box[i]
    return focusing_power(boxes)


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
