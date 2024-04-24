
import os
import re
import sys
import itertools

sys.path.append('../Advent of Code')
from advent_helpers import neighbors


def next_list_item(input_list):
    if len(set(input_list)) == 1:
        return input_list[0]

    return input_list[-1] + next_list_item([input_list[n+1]-input_list[n] for n in range(len(input_list)-1)])


def prev_list_item(input_list):
    if len(set(input_list)) == 1:
        return input_list[0]

    return input_list[0] - prev_list_item([input_list[n+1]-input_list[n] for n in range(len(input_list)-1)])


# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()


accumulator = 0
# Part1
for line in puzzle_input:
    accumulator += next_list_item([int(item) for item in line.strip().split()])

print(f"{day_var} - part 1: {accumulator}")

# Part 2

accumulator = 0
# Part1
for line in puzzle_input:
    accumulator += prev_list_item([int(item) for item in line.strip().split()])

print(f"{day_var} - part 2: {accumulator}")
