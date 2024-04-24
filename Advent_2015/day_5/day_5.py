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
removed_disallowed_substrings = [string.strip() for string in puzzle_input if not re.search(r'(ab|cd|pq|xy)', string)]
ensure_double_substring = [string for string in removed_disallowed_substrings if re.search(r'(\w)\1', string)]
ensure_enough_vowels = [string for string in ensure_double_substring if len(''.join(re.findall(r'[aeiou]', string))) >= 3]

print(f"{day_var} - part 1: {len(ensure_enough_vowels)}")

# Part 2
contains_two_pair = [string.strip() for string in puzzle_input if re.search(r'(\w{2}).*?(\1)', string)]
three_letters = [string.strip() for string in contains_two_pair if re.search(r'(\w).(\1)', string)]

print(f"{day_var} - part 2: {len(three_letters)}")
