
import os
import re
import sys
import itertools

sys.path.append('../Advent of Code')
from advent_helpers import neighbors


def get_path_distance(all_nodes, path):
    distance = 0
    for i in range(len(path)-1):
        distance += all_nodes[(path[i], path[i+1])]
    return distance

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

path_len = 0
# Part1
all_distances = {}
for line in puzzle_input:
    a, b, dist = re.match(r'(\w+) to (\w+) = (\d+)', line).groups()
    all_distances[(a, b)] = int(dist)
    all_distances[(b, a)] = int(dist)

all_destinations = set([i[0] for i in all_distances])
all_paths = itertools.permutations(list(all_destinations))
all_distances = [get_path_distance(all_distances, i) for i in all_paths]

print(f"{day_var} - part 1: {min(all_distances)}")

# Part 2
print(f"{day_var} - part 1: {max(all_distances)}")
