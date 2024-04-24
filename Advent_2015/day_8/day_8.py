
import os
import re
import sys

sys.path.append('../Advent of Code')
from advent_helpers import neighbors

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

# Part1
differences = []
for line in puzzle_input:
    differences.append(len(line.strip()) - len(eval(line.strip())))

print(f"{day_var} - part 1: {sum(differences)}")

# Part 2

differences = []
for line in puzzle_input:
    temp_line = line.strip().strip("\"")
    add_count = 4

    add_count += temp_line.count("\\")
    add_count += temp_line.count("\"")

    add_count += len(temp_line)

    # account for new outer quotes
    add_count += 2
    differences.append(add_count - len(line.strip()))

print(f"{day_var} - part 2: {sum(differences)}")
