import os
import re


# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
test_data = False
puzzle_input = open(f"{day_var}/{day_var}_test_data.txt") if test_data else open(f"{day_var}/{day_var}_data.txt").readlines()
puzzle_input_2 = open(f"{day_var}/{day_var}_part_2_test_data.txt") if test_data else open(f"{day_var}/{day_var}_data.txt").readlines()


def line_value(line):
    nums = re.sub(r'\D', '', line)
    return int(nums[0])*10 + int(nums[-1])


digits = {'oneight': 18, 'twone':21, 'threeight':38, 'fiveight':58, 'sevenine':79, 'eightwo': 82, 'nineight': 98, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
digit_tuple = tuple(digits.keys())
def replace_nums(line):
    if line.startswith(digit_tuple):
        for digit, value in digits.items():
            line = re.sub(rf'^{digit}', str(value), line, 1)
    if line[1:] == '':
        return line
    else:
        return line[0] + replace_nums(line[1:])


# Part 1
calibration_value = 0
for line in puzzle_input:
    temp_value = line_value(line.strip())
    if test_data:
        print(f"{line.strip()} - {temp_value}")
    calibration_value += temp_value

print(f"{day_var} - part 1: {calibration_value!r}")


# Part 2
calibration_value = 0
for line in puzzle_input_2:
    new_line = replace_nums(line.strip())
    temp_value = line_value(new_line)
    if test_data:
        print(f"{line.strip()} - {temp_value}")
    calibration_value += temp_value

print(f"{day_var} - part 2: {calibration_value!r}")
