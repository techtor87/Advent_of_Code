
import os
import re
import sys

sys.path.append('../Advent of Code')
from advent_helpers import neighbors

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()


houses_set = set()
current_location = 0 + 0j
houses_set.add(current_location)
# Part1
for i in range(len(puzzle_input)):
    if puzzle_input[i] == '<':
        current_location = current_location - 1
        houses_set.add(current_location)
    elif puzzle_input[i] == '>':
        current_location = current_location + 1
        houses_set.add(current_location)
    elif puzzle_input[i] == '^':
        current_location = current_location + 1j
        houses_set.add(current_location)
    elif puzzle_input[i] == 'v':
        current_location = current_location - 1j
        houses_set.add(current_location)

print(f"{day_var} - part 1: {len(houses_set)}")

# Part 2

santa_set = set()
robo_set = set()
current_santa = current_robo = 0 + 0j
santa_set.add(current_santa)
robo_set.add(current_robo)
# Part1
for i in range(len(puzzle_input)):
    if i % 2:
        current_location = current_robo
    else:
        current_location = current_santa

    if puzzle_input[i] == '<':
        current_location = current_location - 1
    elif puzzle_input[i] == '>':
        current_location = current_location + 1
    elif puzzle_input[i] == '^':
        current_location = current_location + 1j
    elif puzzle_input[i] == 'v':
        current_location = current_location - 1j

    if i % 2:
        current_robo = current_location
        robo_set.add(current_robo)
    else:
        current_santa = current_location
        santa_set.add(current_santa)


value = 0
print(f"{day_var} - part 2: {len(santa_set.union(robo_set))}")
