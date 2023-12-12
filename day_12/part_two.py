""" Solution to part two of day 12 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import functools
import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 12
CORRECT_EXAMPLE_ANSWER = 525152


def reduce_condition_and_groups(cond, group):
    items = list(filter(None, ''.join(cond).split('.')))
    start = 0
    wildcard_found = False
    while not wildcard_found and start < len(items):
        if '?' in items[start]:
            wildcard_found = True
        else:
            start += 1
    end = len(items)-1
    wildcard_found = False
    while not wildcard_found and end >= 0:
        if '?' in items[end]:
            wildcard_found = True
        else:
            end -= 1
    return (
        '.'+'.'.join(items[start:end+1])+'.',
        group[start:len(group)-(len(items)-end)+1]
        )


@functools.cache
def place_block(cond, group):
    if len(group) == 0:
        if '#' in cond:
            return 0
        else:
            return 1
    if sum(group)+(len(group)-1) >= len(cond):
        return 0
    g = group[0]
    arrangements = 0
    for i in range(len(cond)-g-1):
        placable = True
        if '#' in cond[:i]:
            break
        if cond[i] not in '?.':
            continue
        for k in range(g):
            if cond[i+k+1] not in '?#':
                placable = False
        if not placable:
            continue
        if cond[i+1+g] not in '?.':
            continue
        if placable:
            arrangements += place_block('.'+cond[i+1+g+1:], group[1:])
    return arrangements


def solve(lines):
    conditions = [line.split()[0] for line in lines]
    groups = [list(map(int, line.split()[1].split(','))) for line in lines]
    unfolded_cond = [x+'?'+x+'?'+x+'?'+x+'?'+x for x in conditions]
    unfolded_groups = [g+g+g+g+g for g in groups]
    records = []
    for c, g in zip(unfolded_cond, unfolded_groups):
        records.append(reduce_condition_and_groups(c, g))
    return sum([place_block(r[0], tuple(r[1])) for r in records])


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
