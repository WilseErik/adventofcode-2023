""" Solution to part two of day 18 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """


import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 18
CORRECT_EXAMPLE_ANSWER = 952408144115

def solve(input_lines):
    dir_vectors = {'3':(0, 1), '0':(1, 0), '1':(0, -1), '2':(-1, 0)}
    instructions = []
    for line in input_lines:
        items = line.split()
        v = dir_vectors[items[2][-2]]
        n = int(items[2][2:-2], 16)
        instructions.append(
            {
            'direction':items[0],
            'steps':n,
            'color':items[2],
            'dir_v':v,
            'vector':(v[0]*n, v[1]*n)
            })
    x, y = 0, 0
    verticies = [(x, y)]
    perimiter = 0
    for instr in instructions:
        x += instr['vector'][0]
        y += instr['vector'][1]
        verticies.append((x, y))
        perimiter += instr['steps']
    area = 0
    for i in range(len(verticies)-1):
        k=i+1
        area += (verticies[i][0]*verticies[k][1] - verticies[k][0]*verticies[i][1])
    area += (verticies[-1][0]*verticies[0][1] - verticies[0][0]*verticies[-1][1])
    return abs(area/2)+perimiter/2+1


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
