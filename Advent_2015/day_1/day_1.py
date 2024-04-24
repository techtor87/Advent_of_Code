
import os
import re
import sys

# sys.path.append('../Advent 2015')
# from advent_helpers import neighbors

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()

# Part1
cur_floor = 0
for i in range(len(puzzle_input)):
    if puzzle_input[i] == '(':
        cur_floor += 1
    elif puzzle_input[i] == ')':
        cur_floor -= 1

print(f"{day_var} - part 1: {cur_floor}")

# Part 2

cur_floor = 0
for i in range(len(puzzle_input)):
    if puzzle_input[i] == '(':
        cur_floor += 1
    elif puzzle_input[i] == ')':
        cur_floor -= 1
    if cur_floor < 0:
        print(i)
        break

print(f"{day_var} - part 2: {cur_floor}")
