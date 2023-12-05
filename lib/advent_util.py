""" Utility functions for solving the advent of code puzzels """

import time
import aocd


def run(input_file, solve, correct_example_answer, current_day):
    with open(input_file, 'r') as f:
        example_input_lines = f.readlines()
    start = time.time()
    example_answer = [line.strip() for line in example_input_lines]
    example_answer = solve(example_input_lines)
    time_spent = time.time() - start
    print(f'Example answer = {example_answer}\n    time: {time_spent}')
    assert example_answer == correct_example_answer
    puzzle_input_lines = aocd.get_data(day=current_day, year=2023).split('\n')
    start = time.time()
    puzzle_answer = solve(puzzle_input_lines)
    time_spent = time.time() - start
    print(f'Puzzle answer = {puzzle_answer}\n    time: {time_spent}')
