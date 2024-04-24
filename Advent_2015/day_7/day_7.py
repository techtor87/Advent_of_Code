
import os
import re
import sys

sys.path.append('../Advent of Code')
from advent_helpers import neighbors

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
part2 = True
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_data_part2.txt").readlines() if part2 else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

parsed_commands = []
# Part1
for line in puzzle_input:
    if assignment_parts := re.search(r'^(\w+) -> (\w+)', line):
        parts = assignment_parts.groups()
        parsed_line = f'{parts[1].upper()} = {parts[0].upper()}'
    elif and_parts := re.search(r'^(\w+) AND (\w+) -> (\w+)', line):
        parts = and_parts.groups()
        parsed_line = f'{parts[2].upper()} = {parts[0].upper()} & {parts[1].upper()}'
    elif or_parts := re.search(r'^(\w+) OR (\w+) -> (\w+)', line):
        parts = or_parts.groups()
        parsed_line = f'{parts[2].upper()} = {parts[0].upper()} | {parts[1].upper()}'
    elif lshift_parts := re.search(r'^(\w+) LSHIFT (\w+) -> (\w+)', line):
        parts = lshift_parts.groups()
        parsed_line = f'{parts[2].upper()} = {parts[0].upper()} << {parts[1].upper()}'
    elif rshift_parts := re.search(r'^(\w+) RSHIFT (\w+) -> (\w+)', line):
        parts = rshift_parts.groups()
        parsed_line = f'{parts[2].upper()} = {parts[0].upper()} >> {parts[1].upper()}'
    elif not_parts := re.search(r'^NOT (\w+) -> (\w+)', line):
        parts = not_parts.groups()
        parsed_line = f'{parts[1].upper()} = ~ {parts[0].upper()}'
    else:
        print(f'NOT PARSED: {line}')

    parsed_commands.append(parsed_line)

parsed_commands.sort()
while len(parsed_commands) > 0:
    for cmds in parsed_commands:
        try:
            exec(cmds)
            parsed_commands.remove(cmds)
        except NameError as err:
            pass
        except Exception as err:
            pass
    else:
        pass


print(f"{day_var} - part {2 if part2 else 1}: {A}")
