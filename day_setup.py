import os
import sys


boiler_plate = """
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
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

# Part1


value = 0
print(f"{day_var} - part 1: {value}")

# Part 2




value = 0
print(f"{day_var} - part 2: {value}")

"""

day_value = sys.argv[1]
os.mkdir(day_value)
os.chdir(day_value)
open(f"{day_value}_test_data.txt", "w")
open(f"{day_value}_data.txt", "w")
with open(f"{day_value}.py", "w") as f:
    f.write(boiler_plate)
