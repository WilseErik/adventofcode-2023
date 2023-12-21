""" Solution to part one of day 21 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import numpy as np
import sys
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 21
CORRECT_EXAMPLE_ANSWER = 16


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


def create_node_grid(grid):
    n_grid = []
    for r, row in enumerate(grid):
        node_row = []
        for c, cell in enumerate(row):
            node_row.append(Node(r, c, cell))
        n_grid.append(node_row)
    return n_grid


def solve(input_lines):
    # Create nodes
    grid = [list(row) for row in input_lines]
    even_node_grid = create_node_grid(grid)
    odd_node_grid = create_node_grid(grid)
    start_node = [n for row in even_node_grid for n in row if n.node_type=='S'][0]
    # Add edges
    row_count = len(even_node_grid)
    col_count = len(even_node_grid[0])
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
    # Run a BFS
    if row_count == 11:
        target_steps = 6
    else:
        target_steps = 64
    border = [start_node]
    start_node.value = 0
    for step in range(target_steps):
        new_border = []
        for n in border:
            for e in n.edges:
                if e.value == Node.NO_VALUE:
                    e.value = step + 1
                    new_border.append(e)
        border = new_border
    # Count valid target nodes
    count = 0
    for r in range(row_count):
        for c in range(col_count):
            if even_node_grid[r][c].value != Node.NO_VALUE:
                count += 1
    return count

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
