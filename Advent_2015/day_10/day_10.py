
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
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()
puzzle_input = '1' if test_data else '1113122113'
current_string = puzzle_input
new_input = ''
# Part1
for i in range(50):
    while len(current_string):
        next_char = re.match(rf'^({current_string[0]}+)', current_string).group(1)
        new_input += f'{len(next_char)}{next_char[0]}'
        current_string = current_string[len(next_char):]
    current_string = new_input
    new_input = ''

print(f"{day_var} - part 1: {len(current_string)}")

# Part 2




value = 0
print(f"{day_var} - part 2: {value}")
