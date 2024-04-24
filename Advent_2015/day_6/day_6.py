
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
grid = [[False for i in range(1000)] for j in range(1000)]
for line in puzzle_input:
    startx, starty, endx, endy = [int(i) for i in re.search(r'(\d+),(\d+) through (\d+),(\d+)', line).groups()]

    if 'on' in line:
        for y in range(starty, endy+1):
            for x in range(startx, endx+1):
                grid[y][x] = True
    elif 'off' in line:
        for y in range(starty, endy+1):
            for x in range(startx, endx+1):
                grid[y][x] = False
    elif 'toggle' in line:
        for y in range(starty, endy+1):
            for x in range(startx, endx+1):
                grid[y][x] = not grid[y][x]

print(f"{day_var} - part 1: {sum([i.count(True) for i in grid])}")

# Part 2

dim_grid = [[0 for i in range(1000)] for j in range(1000)]
for line in puzzle_input:
    startx, starty, endx, endy = [int(i) for i in re.search(r'(\d+),(\d+) through (\d+),(\d+)', line).groups()]

    if 'on' in line:
        for y in range(starty, endy+1):
            for x in range(startx, endx+1):
                dim_grid[y][x] += 1
    elif 'off' in line:
        for y in range(starty, endy+1):
            for x in range(startx, endx+1):
                if dim_grid[y][x] > 0:
                    dim_grid[y][x] -= 1
    elif 'toggle' in line:
        for y in range(starty, endy+1):
            for x in range(startx, endx+1):
                dim_grid[y][x] += 2

print(f"{day_var} - part 1: {sum([sum(i) for i in dim_grid])}")
