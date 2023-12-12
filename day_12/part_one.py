""" Solution to part one of day 12 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 12
CORRECT_EXAMPLE_ANSWER = 21

def count_groups(cond):
    return [len(x) for x in filter(None, ''.join(cond).split('.'))]

def count_arrangements(cond, group):
    wildcard_idx = [i for i in range(len(cond)) if cond[i]=='?']
    assert 0 != len(wildcard_idx)
    condition = list(cond)
    count = 0
    for i in range(1 << len(wildcard_idx)):
        for k, w in enumerate(wildcard_idx):
            condition[w] = '.' if (i >> k) & 1 == 0 else '#'
        if count_groups(condition) == group:
            count = count + 1
    return count

def solve(lines):
    conditions = [line.split()[0] for line in lines]
    groups = [list(map(int, line.split()[1].split(','))) for line in lines]
    return sum([count_arrangements(c, g) for c, g in zip(conditions, groups)])

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
