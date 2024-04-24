
import os
import re
import sys
import itertools

sys.path.append('../Advent of Code')
from advent_helpers import neighbors


def calculate_coordinates(input, empty_multiplier):
    coordinates = []
    row_value = -1
    for row in range(len(input)):
        if '#' not in input[row]:
            row_value += empty_multiplier
        else:
            row_value += 1

        for column in range(len(input[row])):
            if input[row][column] == '#':
                coordinates.append((column+(input[row][:column].count('*') * (empty_multiplier-1)), row_value))
    return coordinates


# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

puzzle_input = [line.strip() for line in puzzle_input]
for i in range(len(puzzle_input[0])-1, 0, -1):
    column = [row[i] for row in puzzle_input]
    if '#' not in column:
        for row in range(len(puzzle_input)):
            puzzle_input[row] = puzzle_input[row][:i] + '*' + puzzle_input[row][i+1:]

# Part1
empty_multiplier = 2
galaxy_coordinates = calculate_coordinates(puzzle_input, empty_multiplier)

total_distance = 0
for i, galaxy in enumerate(galaxy_coordinates):
    for other_galaxy in galaxy_coordinates[i:]:
        total_distance += abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])

print(f"{day_var} - part 1: {total_distance}")

# Part 2
empty_multiplier = 1000000
galaxy_coordinates = calculate_coordinates(puzzle_input, empty_multiplier)

total_distance = 0
for i, galaxy in enumerate(galaxy_coordinates):
    for other_galaxy in galaxy_coordinates[i:]:
        total_distance += abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])


print(f"{day_var} - part 2: {total_distance}")
