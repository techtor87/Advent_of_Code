
import os
import re
import sys

sys.path.append('../Advent of Code')
from advent_helpers import neighbors


def run_race(race, distance):
    number_of_wins = 0
    for hold_time in range(race):
        if (race-hold_time)*hold_time  > distance:
            number_of_wins += 1
    return number_of_wins

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

# Part1
race_time = [int(i) for i in re.findall(r'\d+', puzzle_input[0])]
race_distance = [int(i) for i in re.findall(r'\d+', puzzle_input[1])]

all_races = []
total_value = 1
for race, distance in zip(race_time, race_distance):
    winning_time = run_race(race, distance)
    all_races.append(winning_time)
    total_value *= winning_time
value = 0
print(f"{day_var} - part 1: {total_value}")

# Part 2
race_time = int(re.sub(' ', '', puzzle_input[0].split(':')[1]).strip())
race_distance = int(re.sub(' ', '', puzzle_input[1].split(':')[1]).strip())

part_2_result = run_race(race_time, race_distance)
print(f"{day_var} - part 2: {part_2_result}")
