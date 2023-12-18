""" Solution to part one of day 18 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
from matplotlib import pyplot as plt
import numpy as np
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 18
CORRECT_EXAMPLE_ANSWER = 62

def solve(input_lines):
    dir_vectors = {'U':(0, 1), 'R':(1, 0), 'D':(0, -1), 'L':(-1, 0)}
    instructions = []
    for line in input_lines:
        items = line.split()
        v = dir_vectors[items[0]]
        n = int(items[1])
        instructions.append(
            {
            'direction':items[0],
            'steps':n,
            'color':items[2],
            'dir_v':v,
            'vector':(v[0]*n, v[1]*n)
            })
    x, y = 0, 0
    x_min, x_max, y_min, y_max = 0, 0, 0, 0
    for instr in instructions:
        x += instr['vector'][0]
        y += instr['vector'][1]
        x_min = min(x, x_min)
        y_min = min(y, y_min)
        x_max = max(x, x_max)
        y_max = max(y, y_max)
    print(x_min, x_max, y_min, y_max)
    x_offset = -x_min+10
    y_offset = -y_min+10
    x_mid = int((x_max-x_min)/2) +10
    y_mid = int((y_max-y_min)/2) +10
    #
    # Dig perimeter
    #
    dig_site = np.zeros((x_max-x_min+20, y_max-y_min+20), dtype=np.uint8)
    x, y = x_offset, y_offset
    for instr in instructions:
        for _ in range(instr['steps']):
            dig_site[x, y] = 1
            x += instr['dir_v'][0]
            y += instr['dir_v'][1]
            print(x, y)
    #
    # Flood fill
    #
    node = (x_mid, y_mid)
    fill_nodes = [node]
    while len(fill_nodes) != 0:
        x, y = fill_nodes.pop()
        dig_site[x, y] = 2
        if dig_site[x+1, y]==0:
            fill_nodes.append((x+1, y))
        if dig_site[x-1, y]==0:
            fill_nodes.append((x-1, y))
        if dig_site[x, y+1]==0:
            fill_nodes.append((x, y+1))
        if dig_site[x, y-1]==0:
            fill_nodes.append((x, y-1))
    #
    # Count volume
    #
    volume = 0
    for x in range(dig_site.shape[0]):
        for y in range(dig_site.shape[1]):
            if dig_site[x, y]!=0:
                volume += 1
    print(volume)
    plt.imshow(dig_site, interpolation='nearest')
    plt.show()
    return volume

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
