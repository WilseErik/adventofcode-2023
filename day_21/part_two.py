""" Solution to part two of day 21 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import numpy as np
from matplotlib import pyplot as plt
import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 21
CORRECT_EXAMPLE_ANSWER = 2


class Node:
    NO_VALUE = '-'

    def __init__(self, r, c, node_type):
        self.row = r
        self.col = c
        self.node_type = node_type
        self.value = Node.NO_VALUE
        self.edges = []

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return self.node_type
        return str((self.row, self.col, self.cost, self.value))

expansion = 9

def create_node_grid(grid):
    global expansion
    n_grid = []
    for r, row in enumerate(grid*expansion):
        node_row = []
        for c, cell in enumerate(row*expansion):
            node_row.append(Node(r, c, cell))
        n_grid.append(node_row)
    return n_grid


def solve(input_lines):
    global expansion
    # Create nodes
    grid = [list(row) for row in input_lines]
    even_node_grid = create_node_grid(grid)
    odd_node_grid = create_node_grid(grid)
    row_count = len(even_node_grid)
    col_count = len(even_node_grid[0])
    start_l = int((row_count/expansion)*int(expansion/2))
    start_h = int((row_count/expansion)*int(expansion/2+1))
    start_node = [n for row in even_node_grid[start_l:start_h] for n in row[start_l:start_h] if n.node_type=='S'][0]
    #
    # Add edges
    #
    for r in range(row_count):
        for c in range(col_count):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                if (0 <= (r+dr) < row_count) and (0 <= (c+dc) < col_count):
                    n_even = even_node_grid[r+dr][c+dc]
                    n_odd = odd_node_grid[r+dr][c+dc]
                    if n_even.node_type != '#':
                        odd_node_grid[r][c].edges.append(n_even)
                    if n_odd.node_type != '#':
                        even_node_grid[r][c].edges.append(n_odd)
    #
    # Run a BFS
    #
    target_steps = 65+((expansion-1)//2)*131
    border = [start_node]
    start_node.value = 2
    for step in range(target_steps):
        new_border = []
        for n in border:
            for e in n.edges:
                if e.value == Node.NO_VALUE:
                    e.value = step + 1
                    new_border.append(e)
        border = new_border
    #
    # Count valid target nodes
    #
    cound_grid = even_node_grid
    if target_steps % 2 != 0:
        cound_grid = odd_node_grid
    count = 0
    block_count = []
    for block_row in range(expansion):
        rc = []
        for block_col in range(expansion):
            count = 0
            for r in range(131):
                for c in range(131):
                    if cound_grid[block_row*131+r][block_col*131+c].value != Node.NO_VALUE:
                        count += 1
            rc.append(count)
        block_count.append(rc)
    for b in block_count:
        print(' '.join(['{:04}'.format(x) for x in b]))
    full_even = block_count[4][4]
    full_odd = block_count[3][4]
    left_corner = block_count[4][0]
    right_corner = block_count[4][-1]
    up_corner = block_count[0][4]
    down_corner = block_count[-1][4]
    lu_a = block_count[3][0]
    lu_b = block_count[3][1]
    ld_a = block_count[5][0]
    ld_b = block_count[5][1]

    ru_a = block_count[3][-1]
    ru_b = block_count[3][-2]
    rd_a = block_count[5][-1]
    rd_b = block_count[5][-2]

    expansion = 2*(26501365-65)//131+1

    n_a = (expansion-1)//2
    n_b = (expansion-1)//2-1
    r = expansion//2
    n_even = 1 + 4*(r//2)*(r//2-1)
    n_odd = 4*((r+1)//2)*((r+1)//2)
    print('corners', left_corner, right_corner, up_corner, down_corner)
    print('full blocks', n_a, n_b, n_even, n_odd)
    print('side blocks', lu_a, lu_b, ld_a, ld_b, ru_a, ru_b, rd_a, rd_b)
    A = (lu_a+ld_a+ru_a+rd_a)*n_a
    B = (lu_b+ld_b+ru_b+rd_b)*n_b
    C = (left_corner+right_corner+up_corner+down_corner)
    E = full_even*n_even
    O = full_odd*n_odd
    print('parts', A, B, C, E, O)
    total = (
        (lu_a+ld_a+ru_a+rd_a)*n_a +
        (lu_b+ld_b+ru_b+rd_b)*n_b +
        (left_corner+right_corner+up_corner+down_corner) +
        (full_even*n_even + full_odd*n_odd))
    print('total',  total)
    block_total = 0
    for block_row in block_count:
        for x in block_row:
            block_total += x
    print('block total', block_total)
    for r in range(row_count):
        for c in range(col_count):
            if cound_grid[r][c].value != Node.NO_VALUE:
                count += 1
    #
    # Generate image
    #
    img = np.zeros((col_count, row_count, 3), dtype=np.uint8)
    for r in range(row_count):
        for c in range(col_count):
            n = cound_grid[r][c]
            v = n.value
            if r % 131 == 0 or r%131==130 or c%131 == 0 or c%131==130:
                img[c, r, 0] = 0
                img[c, r, 1] = 0
                img[c, r, 2] = 0
            elif n.node_type == '#':
                img[c, r, 1] = 50
                img[c, r, 1] = 50
                img[c, r, 1] = 50
            elif Node.NO_VALUE == v:
                img[c, r, 0] = 255
                img[c, r, 1] = 255
                img[c, r, 2] = 255
            else:
                img[c, r, 0] = v
                img[c, r, 1] = 100
                img[c, r, 2] = 255#v
    plt.imshow(img, interpolation='nearest')
    plt.show()
    print('count', count)
    #[print(''.join([str(c) for c in row])) for row in even_node_grid]
    #[print(''.join(['O' if c.value != Node.NO_VALUE else '_' for c in row])) for row in even_node_grid]
    return 1


if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
