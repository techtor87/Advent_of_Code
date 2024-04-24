import math
import os
import re
import sys

sys.path.append('../Advent of Code')
from advent_helpers import neighbors

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
part_2 = True
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
if part_2 :
    puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data_part_2.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()
else:
    puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

move_instruction = puzzle_input[0].strip()
map_dict = {}
for line in puzzle_input[2:]:
    loc, node = line.strip().split(' = ')
    left, right = node.strip('(').strip(')').split(', ')
    map_dict[loc] = (left, right)

# Part1
if not part_2:
    current_location = "AAA"
    count = 0
    while current_location != 'ZZZ':
        current_location = map_dict[current_location][(1 if move_instruction[count % len(move_instruction)] == 'R' else 0)]
        count += 1

    print(f"{day_var} - part 1: {count}")

# Part 2
if part_2:
    current_locations = [node for node in map_dict if node[2] == 'A']
    all_steps = []
    for current_location in current_locations:
        count = 0
        while current_location[2] != 'Z':
            current_location = map_dict[current_location][(1 if move_instruction[count % len(move_instruction)] == 'R' else 0)]
            count += 1
        all_steps.append(count)

    print(f"{day_var} - part 2: {math.lcm(*all_steps)}")
