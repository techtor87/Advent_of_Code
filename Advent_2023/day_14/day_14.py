
import os
import re
import sys
import itertools

sys.path.append('../Advent of Code')
from advent_helpers import neighbors


def slide_rocks_left(array):
    new_array = []
    for row in array:
        clusters = (''.join(row)).split('#')
        new_str = ''
        for substr in clusters:
            rollers = substr.count('O')
            empty = substr.count('.')
            new_str += 'O'*rollers
            new_str += '.'*empty
            new_str += '#'
        new_array.append(list(new_str[:len(row)]))
    return new_array


def rotate_cw(array):
    return list(zip(*array[::-1]))


def rotate_ccw(array):
    return list(zip(*array))[::-1]


# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = True
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

# Part1
rock_array = [[x for x in row.strip()] for row in puzzle_input]
rock_array = rotate_ccw(rock_array)
rock_array = slide_rocks_left(rock_array)

rock_array = rotate_cw(rock_array)
weight = 0
for index, row in enumerate(rock_array):
    for char in row:
        if char == 'O':
            weight += len(rock_array)-index

print(f"{day_var} - part 1: {weight}")

# Part 2
rock_array = [[x for x in row.strip()] for row in puzzle_input]
rock_array = rotate_ccw(rock_array)
rock_array = slide_rocks_left(rock_array)

for i in range(1000000000*4):
    rock_array = rotate_cw(rock_array)
    rock_array = slide_rocks_left(rock_array)

rock_array = rotate_cw(rock_array)
weight = 0
for index, row in enumerate(rock_array):
    for char in row:
        if char == 'O':
            weight += len(rock_array)-index

print(f"{day_var} - part 1: {weight}")


value = 0
print(f"{day_var} - part 2: {value}")
