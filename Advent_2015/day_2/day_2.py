
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
# Part 2
total = 0
total_ribbon = 0
for present in puzzle_input:
    l, w, h = [int(i) for i in present.strip().split('x')]
    side = w*h
    front = l*h
    top = l*w
    extra = min([side, front, top])

    present_total = 2*side + 2*front + 2*top + extra
    total += present_total

    volume = l*w*h
    ribbon_subtotal = volume + 2*min([l+h, h+w, w+l])
    total_ribbon += ribbon_subtotal

print(f"{day_var} - part 1: {total}")
print(f"{day_var} - part 2: {total_ribbon}")
