""" Solution to part one of day 19 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 19
CORRECT_EXAMPLE_ANSWER = 19114

def parse_part_line(line):
    line = line.replace('{', '').replace('}', '')
    items = [int(x.split('=')[1]) for x in line.split(',')]
    return {'x':items[0], 'm':items[1], 'a':items[2], 's':items[3]}


def parse_input(input_lines):
    workflow_lines, part_lines = [x.split()
    for x in '\n'.join(input_lines).split('\n\n')]
    parts = [parse_part_line(s) for s in part_lines]
    workflows = {}
    for line in workflow_lines:
        line = line.replace('}', '')
        name, line = line.split('{')
        workflows[name] = line.split(',')
    return workflows, parts


def process_part(part, all_workflows):
    current_workflow = 'in'
    current_step = 0
    while current_workflow != 'A' and current_workflow != 'R':
        w = all_workflows[current_workflow][current_step]
        if ':' in w:
            statement, label = w.split(':')
            if '>' in statement:
                if part[statement.split('>')[0]] > int(statement.split('>')[1]):
                    current_workflow = label
                    current_step = 0
                else:
                    current_step += 1
            elif '<' in statement:
                if part[statement.split('<')[0]] < int(statement.split('<')[1]):
                    current_workflow = label
                    current_step = 0
                else:
                    current_step += 1
        else:
            current_workflow = w
            current_step = 0
    return current_workflow == 'A'


def solve(input_lines):
    workflows, parts = parse_input(input_lines)
    accumulator = 0
    for part in parts:
        if process_part(part, workflows):
            accumulator += sum(part.values())
    return accumulator


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
