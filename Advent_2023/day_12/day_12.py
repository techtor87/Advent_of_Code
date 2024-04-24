
import os
import re
import sys
import itertools
from collections import deque

sys.path.append('../Advent of Code')
from advent_helpers import neighbors, timeit


def check_solution(solution, position_list):
    # if solution.count('#') != sum(position_list):
        # return False

    solution_list = list(filter(None, solution.split('.')))
    # if len(solution_list) != len(position_list):
        # return False

    for i in range(len(position_list)):
        if solution_list[i].count('#') != position_list[i]:
            return False

    return True

@timeit
def build_layouts(springs, position_list):
    combinations = []
    for i in range(pow(2, sum(position_list)), pow(2, len(springs))):
        combination = bin(i)[2:].zfill(len(springs)).replace('0', '.').replace('1', '#')
        if combination.count('#') != sum(position_list):
            continue

        solution_list = list(filter(None, combination.split('.')))
        if len(solution_list) != len(position_list):
            continue

        for i, char in enumerate(springs):
            if char != '?':
                if char != combination[i]:
                    break
        else:
            combinations.append(combination)

    return combinations

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False

# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

# Part1
counter = 0
for line in puzzle_input:
    springs, positions_str = line.strip().split(" ")
    positions = [int(pos) for pos in positions_str.split(',')]
    possible_spring_layout = build_layouts(springs, positions)

    for layout in possible_spring_layout:
        if check_solution(layout, positions):
            counter += 1


print(f"{day_var} - part 1: {counter}")

# Part 2

counter = 0
for line in puzzle_input:
    springs, positions_str = line.strip().split(" ")
    springs = springs + '?' + springs + '?' + springs
    positions_str = f'{positions_str},{positions_str},{positions_str}'
    positions = [int(pos) for pos in positions_str.split(',')]
    possible_spring_layout = build_layouts(springs, positions)

    for layout in possible_spring_layout:
        if check_solution(layout, positions):
            counter += 1


print(f"{day_var} - part 1: {counter}")
