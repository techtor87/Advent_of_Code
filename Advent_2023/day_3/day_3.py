
import os
import re
import sys

sys.path.append('../Advent of Code')
from advent_helpers import neighbors


symbols = ['*', '-', '+', '&', '$', '#', '/', '@', '%', '=']
expand_symbols = symbols + ['.']


def expand_value(grid, x_pos, y_pos):
    if grid[y_pos][x_pos] == '.':
        return None

    start = end = x_pos
    start_found = end_found = False
    while not (start_found and end_found):
        if start-1 >= 0:
            if grid[y_pos][start-1] not in expand_symbols:
                start -= 1
            else:
                start_found = True
        else:
            start_found = True

        if end+1 < len(grid[y_pos].strip())-1:
            if grid[y_pos][end+1] not in expand_symbols:
                end += 1
            else:
                end_found = True
        else:
            end_found = True

    return grid[y_pos][start:end+1]


def check_neighbors(neighbors, symbols=symbols):
    for symbol in symbols:
        if symbol in neighbors.values():
            return True
    return False


def convert_to_complex(neighbor_position):
    if neighbor_position == 1:
        return -1-1j
    if neighbor_position == 2:
        return -1j
    if neighbor_position == 3:
        return 1-1j
    if neighbor_position == 4:
        return -1
    if neighbor_position == 5:
        return 0
    if neighbor_position == 6:
        return 1
    if neighbor_position == 7:
        return -1+1j
    if neighbor_position == 8:
        return +1j
    if neighbor_position == 9:
        return 1+1j


def get_index_of_neighbor(neighbors, symbol):
    if symbol in neighbors.values():
        return convert_to_complex(list(neighbors.values()).index(symbol)+1)
    return False


# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
part_1 = False
part_2 = True
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

# Part1
if part_1:
    all_numbers = [int(value.group(0)) for line in puzzle_input for value in re.finditer(r'\d*', line) if value.group(0) != '']
    for line in range(len(puzzle_input)):
        for match in re.finditer(r'\d+', puzzle_input[line]):
            symbol_found = False
            for x_pos in range(match.start(), match.end()):
                neighbor_values = neighbors(puzzle_input, x_pos, line)
                if symbol_found := check_neighbors(neighbor_values):
                    break
            if not symbol_found:
                all_numbers.remove(int(match.group()))

    print(f"{day_var} - part 1: {sum(all_numbers)}")

# Part 2
if part_2:
    gear_ratios = []
    all_gear_numbers = []
    for line_num, line in enumerate(puzzle_input):
        for digit in re.finditer(r'\d+', line):
            for i in range(len(digit.group())):
                if symbol_index := get_index_of_neighbor(neighbors(puzzle_input, i+digit.start(), line_num), '*'):
                    all_gear_numbers.append(((i+digit.start()+line_num*1j)+symbol_index, int(digit.group())))
                    break

    gear_loc_set = set([key[0] for key in all_gear_numbers])
    gear_pairs = [[key for key in all_gear_numbers if key[0] == gear_loc] for gear_loc in list(gear_loc_set)]
    for gear_set in gear_pairs:
        if len(gear_set) == 2:
            gear_ratios.append(gear_set[0][1]*gear_set[1][1])
    print(f"{day_var} - part 2: {sum(gear_ratios)}")
