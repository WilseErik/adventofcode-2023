""" Solution to part two of day 20 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
import time
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 20
CORRECT_EXAMPLE_ANSWER = 1


class Node:
    def __init__(self, line):
        self.type = line[0]
        self.name = line.split()[0].replace('%', '').replace('&', '')
        self.edge_names = line.split('->')[1].strip().split(', ')
        self.edges = []
        self.input_edges = {}
        self.is_on = False


    def process_pulse(self, sender, pulse):
        out_pulses = []
        if self.type == '%':
            if not pulse:
                self.is_on = not self.is_on
                out_pulses = [(self, e, self.is_on) for e in self.edges]
        elif self.type == '&':
            self.input_edges[sender.name] = pulse
            out = not all(self.input_edges.values())
            out_pulses = [(self, e, out) for e in self.edges]
        else:
            out_pulses = [(self, e, pulse) for e in self.edges]
        return out_pulses


    def __repr__(self):
        return self.name


def button_press_turned_machine_on(broadcaster):
    pulses = broadcaster.process_pulse(None, False)
    low_to_rx = False
    while len(pulses) != 0:
        p = pulses.pop(0)
        if p[1].name == 'rx' and p[2]==False:
            low_to_rx = True
        new_pulses = p[1].process_pulse(p[0], p[2])
        for np in new_pulses:
            pulses.append(np)
    return low_to_rx


def solve(input_lines):
    nodes = [Node(line) for line in input_lines]
    # Add missing destingation nodes
    for i in range(len(nodes)):
        n = nodes[i]
        for e in n.edge_names:
            if len(list(filter(lambda x:x.name==e, nodes))) == 0:
                nodes.append(Node('{:} -> dummy'.format(e)))
    # Create input and output edges
    broadcaster = None
    for n in nodes:
        if n.name == 'broadcaster':
            broadcaster = n
        for e in n.edge_names:
            for m in nodes:
                if m.name == e:
                    n.edges.append(m)
                    m.input_edges[n.name] = False
    # Run all button presses
    count = 1
    start = time.time()
    while not button_press_turned_machine_on(broadcaster):
        count += 1
        if count % 10000 == 0:
            print(count, time.time() - start)
    return count

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
