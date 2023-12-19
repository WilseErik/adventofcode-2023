""" Solution to part two of day 19 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position


CURRENT_DAY = 19
CORRECT_EXAMPLE_ANSWER = 167409079868000

def parse_input(input_lines):
    workflow_lines, _ = [x.split()
        for x in '\n'.join(input_lines).split('\n\n')]
    workflows = {}
    for line in workflow_lines:
        line = line.replace('}', '')
        name, line = line.split('{')
        workflows[name] = line.split(',')
    return workflows


def bfs_workflows(workflows):
    unchecked_paths = [('in', 0, [])]
    accept_paths = []
    decline_paths = []
    while len(unchecked_paths) != 0:
        current_workflow, current_step, history = unchecked_paths.pop()
        if current_workflow=='R':
            decline_paths.append(history)
        elif current_workflow=='A':
            accept_paths.append(history)
        else:
            w = workflows[current_workflow][current_step]
            if ':' in w:
                statement, label = w.split(':')
                if '>' in statement:
                    inv_statement = statement.replace('>', '<=')
                else:
                    inv_statement = statement.replace('<', '>=')
                h = [x for x in history]
                h.append(statement)
                h_inv = [x for x in history]
                h_inv.append(inv_statement)
                if '>' in statement:
                    unchecked_paths.append((label, 0, h))
                    unchecked_paths.append(
                        (current_workflow, current_step+1, h_inv))
                elif '<' in statement:
                    unchecked_paths.append((label, 0, h))
                    unchecked_paths.append(
                        (current_workflow, current_step+1, h_inv))
            else:
                unchecked_paths.append((w, 0, history))
    return accept_paths



def solve(input_lines):
    workflows = parse_input(input_lines)
    paths = bfs_workflows(workflows)
    #
    # Convert paths to accepted x,m,a,s ranges
    #
    accept_ranges = []
    for p in paths:
        ranges = {'x':[1,4000], 'm':[1,4000], 'a':[1,4000], 's':[1,4000]}
        for statement in p:
            variable = statement[0]
            value = int(statement.split('=')[-1].split('>')[-1].split('<')[-1])
            if '<' in statement:
                if '=' not in statement:
                    value = value - 1
                if value < ranges[variable][1]:
                    ranges[variable][1] = value
            if '>' in statement:
                if '=' not in statement:
                    value = value + 1
                if value > ranges[variable][0]:
                    ranges[variable][0] = value
        for v in ranges.values():
            assert v[1] > v[0]
        accept_ranges.append(ranges)
    #
    # Sum up all ranges
    #
    total_volume = 0
    for r in accept_ranges:
        total_volume += (
            (r['x'][1]-r['x'][0]+1) *
            (r['m'][1]-r['m'][0]+1) *
            (r['a'][1]-r['a'][0]+1) *
            (r['s'][1]-r['s'][0]+1)
            )
    return total_volume

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
