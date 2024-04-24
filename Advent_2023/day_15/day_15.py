
import os
import re
import sys
import itertools
from collections import OrderedDict

sys.path.append('../Advent of Code')
from advent_helpers import neighbors


def hash_func(str):
    current_value = 0
    for char in str:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

# Part1
steps = puzzle_input.strip().split(',')
total_hash = []
for step in steps:
    total_hash.append(hash_func(step))

print(f"{day_var} - part 1: {sum(total_hash)}")

# Part 2
boxes = [OrderedDict() for i in range(256)]

for step in puzzle_input.strip().split(','):
    if '=' in step:
        parts = step.split('=')
        box = hash_func(parts[0])
        boxes[box][parts[0]] = parts[1]
    elif '-' in step:
        label = step[:-1]
        box = hash_func(label)
        if label in boxes[box]:
            boxes[box].pop(label)
    else:
        pass

values = []
for box_i, box in enumerate(boxes, start=1):
    for slot_i, focal_length in enumerate(box.values(), start=1):
        values.append(box_i * slot_i * int(focal_length))

print(f"{day_var} - part 2: {sum(values)}")
