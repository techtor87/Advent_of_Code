
import os
import re
import sys

sys.path.append('../Advent of Code')
from advent_helpers import neighbors


def parse_map_values(input_str):
    transform_str_list = re.findall(r"\d+ \d+ \d+", input_str.split(':')[1])
    tranform_list = [tuple(int(val) for val in transform_str.split(' ')) for transform_str in transform_str_list]
    return tranform_list


def map_transform(input_value, transform_map):
    for transform in transform_map:
        if transform[1] <= input_value < transform[1]+transform[2]:
            return transform[0] + (input_value-transform[1])
    return input_value


# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
test_data = False
puzzle_input = open(f"{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{day_var}/{day_var}_data.txt").read()
cat_split = puzzle_input.split('\n\n')

seed_list = [int(seed) for seed in re.findall(r'\d+', cat_split[0].split(':')[1])]
seed_to_soil_map = parse_map_values(cat_split[1])
soil_to_fert_map = parse_map_values(cat_split[2])
fert_to_water_map = parse_map_values(cat_split[3])
water_to_light_map = parse_map_values(cat_split[4])
light_to_temp_map = parse_map_values(cat_split[5])
temp_to_humid_map = parse_map_values(cat_split[6])
humid_to_loc_map = parse_map_values(cat_split[7])


# Part1
loc_list = [
    map_transform(
        map_transform(
            map_transform(
                map_transform(
                    map_transform(
                        map_transform(
                            map_transform(seed, seed_to_soil_map),
                            soil_to_fert_map),
                        fert_to_water_map),
                    water_to_light_map),
                light_to_temp_map),
            temp_to_humid_map),
        humid_to_loc_map)
            for seed in seed_list]

loc_list.sort()
print(f"{day_var} - part 1: {loc_list[0]}")

# Part 2
closest_loc = 1166153959
for seed in (seed for i in range(0, len(seed_list), 2) for seed in range(seed_list[i], seed_list[i]+seed_list[i+1])):
    new_loc = map_transform(
        map_transform(
            map_transform(
                map_transform(
                    map_transform(
                        map_transform(
                            map_transform(seed, seed_to_soil_map),
                            soil_to_fert_map),
                        fert_to_water_map),
                    water_to_light_map),
                light_to_temp_map),
            temp_to_humid_map),
        humid_to_loc_map)
    if closest_loc is None:
        closest_loc = new_loc

    if new_loc < closest_loc:
        closest_loc = new_loc

print(f"{day_var} - part 2: {closest_loc}")
