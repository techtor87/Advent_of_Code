
import os
import re
import sys
import itertools

sys.path.append('../Advent of Code')
from advent_helpers import neighbors

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = True
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

# Part1
value = 0
for puzzle in puzzle_input.split('\n\n'):
    puzzle = puzzle.splitlines()
    for i in range(1, len(puzzle)):
        for reflection_count in range(i-1, -1, -1):
            if puzzle[i] != puzzle[reflection_count]:
                break
        else:
            print(f'horizontal reflection found: {i}')

    for i in range(1, len(puzzle[0])):
        for reflection_count in range(i-1, -1, -1):
            if puzzle[i] != puzzle[reflection_count]:
                break
        else:
            print(f'vertical reflection found: {i}')

value = 0
print(f"{day_var} - part 1: {value}")

# Part 2




value = 0
print(f"{day_var} - part 2: {value}")
