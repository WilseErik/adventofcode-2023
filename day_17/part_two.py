""" Solution to part two of day X of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
import colorama
import heapq
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 17
CORRECT_EXAMPLE_ANSWER = 94


class Node:
    def __init__(self, r, c, cost, direction):
        self.row = r
        self.col = c
        self.cost = cost
        self.value = 2**15
        self.edges = []
        self.prev = None
        self.direction = direction

    def __lt__(self, other):
        return self.value < other.value

    def get_dir_str(self):
        return {0:'U', 1:'R', 2:'D', 3:'L'}[self.direction]

    def __repr__(self):
        direction = {0:'U', 1:'R', 2:'D', 3:'L'}
        return str((self.row, self.col, self.cost, self.value, direction[self.direction]))


def create_node_grid(grid, direction):
    n_grid = []
    for r, row in enumerate(grid):
        node_row = []
        for c, cell in enumerate(row):
            node_row.append(Node(r, c, cell, direction))
        n_grid.append(node_row)
    return n_grid


def solve(input_lines):
    #
    # Construct graph
    #
    grid = [list(map(int, row)) for row in input_lines]
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    n_rows = len(grid)
    n_cols = len(grid[0])
    node_grid = [create_node_grid(grid, i) for i in range(4)]
    for r in range(n_rows):
        for c in range(n_cols):
            for d in range(4):
                min_dist = 4
                dist_range = 7
                if (d != UP and d != DOWN) or (r==0 and c == 0):
                    cost = 0
                    for i in range(min_dist-1):
                        if (r-1-i) >= 0:
                            cost += node_grid[UP][r-1-i][c].cost
                    for i in range(dist_range):
                        if (r-min_dist-i) >= 0:
                            cost += node_grid[UP][r-min_dist-i][c].cost
                            node_grid[d][r][c].edges.append((node_grid[UP][r-min_dist-i][c], cost))
                    cost = 0
                    for i in range(min_dist-1):
                        if (r+1+i) < n_rows:
                            cost += node_grid[DOWN][r+1+i][c].cost
                    for i in range(dist_range):
                        if (r+min_dist+i) < n_rows:
                            cost += node_grid[DOWN][r+min_dist+i][c].cost
                            node_grid[d][r][c].edges.append((node_grid[DOWN][r+min_dist+i][c], cost))
                if (d != RIGHT and d != LEFT) or (r==0 and c == 0):
                    cost = 0
                    for i in range(min_dist-1):
                        if (c+1+i) < n_cols:
                            cost += node_grid[RIGHT][r][c+1+i].cost
                    for i in range(dist_range):
                        if (c+min_dist+i) < n_cols:
                            cost += node_grid[RIGHT][r][c+min_dist+i].cost
                            node_grid[d][r][c].edges.append((node_grid[RIGHT][r][c+min_dist+i], cost))
                    cost = 0
                    for i in range(min_dist-1):
                        if (c-1-i) >= 0:
                            cost += node_grid[LEFT][r][c-1-i].cost
                    for i in range(dist_range):
                        if (c-min_dist-i) >= 0:
                            cost += node_grid[LEFT][r][c-min_dist-i].cost
                            node_grid[d][r][c].edges.append((node_grid[LEFT][r][c-min_dist-i], cost))
                    
    end_nodes = [node_grid[i][n_rows-1][n_cols-1] for i in range(4)]
    #
    # Run path finding
    #
    start_node = node_grid[UP][0][0]
    unchecked_nodes = []
    checked_nodes = set()
    heapq.heapify(unchecked_nodes)
    heapq.heappush(unchecked_nodes, (0, start_node))
    while len(unchecked_nodes) > 0:
        # print(len(unchecked_nodes))
        v, n = heapq.heappop(unchecked_nodes)
        if n not in checked_nodes:
            checked_nodes.add(n)
            for edge, cost in n.edges:
                if edge not in checked_nodes  and v + cost < edge.value:
                       edge.value = v + cost
                       edge.prev = n
                       heapq.heappush(unchecked_nodes, (v + cost, edge))
    paths_found = [x.value!=2**15 for x in end_nodes]
    #
    # Print
    #
    print([n.value for n in end_nodes])
    n = end_nodes[2]
    path = set()
    path_nodes = []
    while n.prev != None:
        #print(n)
        path.add((n.row, n.col))
        path_nodes.append(n)
        n = n.prev
    colorama.init()
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if (r,c) not in path:
                print(colorama.Fore.WHITE + str(v), end='')
            else:
                nodes = [n for n in path_nodes if n.row==r and n.col == c]
                print(colorama.Fore.GREEN + nodes[0].get_dir_str(), end='')
        print('')
    print(colorama.Style.RESET_ALL)
    return min([n.value for n in end_nodes])

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
