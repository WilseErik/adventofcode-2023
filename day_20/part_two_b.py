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
            self.input_edges[sender] = pulse
            out = not all(self.input_edges.values())
            self.is_on = out
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
        if p[1].name == 'mm' and p[2]==False:
            low_to_rx = True
        new_pulses = p[1].process_pulse(p[0], p[2])
        for np in new_pulses:
            pulses.append(np)
    return low_to_rx


def reset_all_nodes(nodes):
    for n in nodes:
        n.is_on = False
        for key in n.input_edges:
            n.input_edges[key] = False


def solve(input_lines):
    nodes = [Node(line) for line in input_lines]
    # Add missing destingation nodes
    for i in range(len(nodes)):
        n = nodes[i]
        for e in n.edge_names:
            if len(list(filter(lambda x:x.name==e, nodes))) == 0:
                nodes.append(Node('{:} -> dummy'.format(e)))
    #
    # Create input and output edges
    #
    broadcaster = None
    for n in nodes:
        if n.name == 'broadcaster':
            broadcaster = n
        for e in n.edge_names:
            for m in nodes:
                if m.name == e:
                    n.edges.append(m)
                    m.input_edges[n] = False
    #
    # Trace back required state
    #
    print(nodes)
    end_node = list(filter(lambda x:x.name=='mm', nodes))[0]
    unchecked = [(e, False) for e in end_node.input_edges]
    required_states = []
    while len(unchecked) != 0:
        node, output = unchecked.pop()
        print('===============')
        print(node, output)
        print(unchecked)
        print('...')
        if node.type == '&':
            if not output:
                # all inputs must be high
                for e in node.input_edges:
                    unchecked.append((e, True))
                    print(e, True)
            else:
                # all inputs cant be high
                assert len(node.input_edges) == 1
                unchecked.append((list(node.input_edges.keys())[0], False))
                print(node, False)
        elif node.type == '%':
            if len([s for s in required_states if s[0].name == node.name]) == 0:
                required_states.append((node, output))
                assert output is True
    print(required_states)
    #
    # Cycle detection for each state
    #
    cycles = []
    print('required_states', required_states)
    for n, target_state in required_states:
        reset_all_nodes(nodes)
        print('analysing state', n.name)
        count = 0
        while target_state is not n.is_on:
            button_press_turned_machine_on(broadcaster)
            count += 1
        while target_state is n.is_on:
            button_press_turned_machine_on(broadcaster)
            count += 1
        offset = count
        print(count)
        count = 0
        while target_state is not n.is_on:
            button_press_turned_machine_on(broadcaster)
            count += 1
        first_on = count
        print(count)
        while target_state is n.is_on:
            button_press_turned_machine_on(broadcaster)
            count += 1
        print(count)
        cycles.append((offset-count, count, first_on))
    print(cycles)

    #
    # Cycle detection for each state
    #
    not_coprime_states = [(r[0], c) for r, c in zip(required_states, cycles) if c[1]%2==0]
    coprime_states = [(r[0], c) for r, c in zip(required_states, cycles) if c[1]%2!=0]
    print('================================')
    print('not_coprime_states')
    for x in not_coprime_states:
        print(x)
    print('================================')
    print('coprime_states')
    for x in coprime_states:
        print(x)

    # Run all button presses
    out_lines = []
    count = 1
    reset_all_nodes(nodes)
    start = time.time()
    while not button_press_turned_machine_on(broadcaster):
        count += 1
        #line = ''
        #for req in required_states:
        #    if req[0].is_on:
        #        line += '1'
        #    else:
        #        line += '0'
        out_lines.append(str(end_node.is_on)+'\n')
        if count % (10000) == 0:
            print(count, time.time() - start)
            break
    with open('testa.txt', 'w') as f:
        f.writelines(out_lines)
    return count

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)
