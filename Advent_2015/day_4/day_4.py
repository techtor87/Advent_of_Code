
import os
import re
import sys
import hashlib

sys.path.append('../Advent of Code')
from advent_helpers import neighbors

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = True
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

puzzle_input = 'ckczppom'

# Part1
count = 1
while True:
    if result := hashlib.md5(f'{puzzle_input}{count}'.encode()).hexdigest():
        if result.startswith('000000'):
            break
    count += 1

print(f"{day_var} - part 1: {count}")

# Part 2




value = 0
print(f"{day_var} - part 2: {value}")
