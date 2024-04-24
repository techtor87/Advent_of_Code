import os
import re
import sys
import itertools

sys.path.append('../Advent of Code')
from advent_helpers import neighbors


def move_point(point_symbol, point_address, previous_point):
    possible_points = []
    if point_symbol == '.':
        pass
    elif point_symbol == '|':
        possible_points.append((point_address[0], point_address[1]-1))
        possible_points.append((point_address[0], point_address[1]+1))
    elif point_symbol == '-':
        possible_points.append((point_address[0]-1, point_address[1]))
        possible_points.append((point_address[0]+1, point_address[1]))
    elif point_symbol == 'L':
        possible_points.append((point_address[0], point_address[1]-1))
        possible_points.append((point_address[0]+1, point_address[1]))
    elif point_symbol == 'J':
        possible_points.append((point_address[0]-1, point_address[1]))
        possible_points.append((point_address[0], point_address[1]-1))
    elif point_symbol == '7':
        possible_points.append((point_address[0]-1, point_address[1]))
        possible_points.append((point_address[0], point_address[1]+1))
    elif point_symbol == 'F':
        possible_points.append((point_address[0]+1, point_address[1]))
        possible_points.append((point_address[0], point_address[1]+1))
    elif point_symbol == 'S':
        pass

    return (possible_points[0] if possible_points[0] != previous_point else possible_points[1], point_address)

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = True
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

for i, line in enumerate(puzzle_input):
    if 'S' in line:
        start_point = (line.index('S'), i)
        break

neighbor = neighbors(puzzle_input, start_point[0], start_point[1])

if neighbor['2'] in ['|', 'F', '7']:
    current_point = (start_point[0], start_point[1]-1)
elif neighbor['4'] in ['-', 'F', 'L']:
    current_point = (start_point[0]-1, start_point[1])
elif neighbor['6'] in ['-', 'J', '7']:
    current_point = (start_point[0]+1, start_point[1])
elif neighbor['8'] in ['|', 'L', 'J']:
    current_point = (start_point[0], start_point[1]+1)

previous_point = start_point
pipe_counter = 1
visited_points = []
# print(f'{puzzle_input[start_point[1]][start_point[0]]} : {start_point} -> {current_point}')
# Part1
while current_point != start_point:
    current_point, previous_point = move_point(puzzle_input[current_point[1]][current_point[0]], current_point, previous_point)
    visited_points.append(current_point)
    pipe_counter += 1
    # print(f'{puzzle_input[previous_point[1]][previous_point[0]]} : {previous_point} -> {current_point}')

print(f"{day_var} - part 1: {pipe_counter/2}")

# Part 2
graph = [[puzzle_input[rows][cell] for cell in range(len(puzzle_input[0]))] for rows in range(len(puzzle_input))]
for row in range(len(graph)):
    for line in range(len(graph[row])):
        if (row, line) not in visited_points:
            graph[row][line] = '.'

expanded_graph = [['.' for cell in range(len(puzzle_input[0])*3)] for rows in range(len(puzzle_input)*3)]

for y in range(len(graph)):
    for x, cell in enumerate(graph[y]):
        if cell == '.':
            pass
        elif cell == '|':
            expanded_graph[y*3][x*3] = '.'
            expanded_graph[y*3][x*3+1] = '|'
            expanded_graph[y*3][x*3+2] = '.'
            expanded_graph[y*3+1][x*3] = '.'
            expanded_graph[y*3+1][x*3+1] = '|'
            expanded_graph[y*3+1][x*3+2] = '.'
            expanded_graph[y*3+2][x*3] = '.'
            expanded_graph[y*3+2][x*3+1] = '|'
            expanded_graph[y*3+2][x*3+2] = '.'
        elif cell == '-':
            expanded_graph[y*3][x*3] = '.'
            expanded_graph[y*3][x*3+1] = '.'
            expanded_graph[y*3][x*3+2] = '.'
            expanded_graph[y*3+1][x*3] = '-'
            expanded_graph[y*3+1][x*3+1] = '-'
            expanded_graph[y*3+1][x*3+2] = '-'
            expanded_graph[y*3+2][x*3] = '.'
            expanded_graph[y*3+2][x*3+1] = '.'
            expanded_graph[y*3+2][x*3+2] = '.'
        elif cell == 'F':
            expanded_graph[y*3][x*3] = '.'
            expanded_graph[y*3][x*3+1] = '.'
            expanded_graph[y*3][x*3+2] = '.'
            expanded_graph[y*3+1][x*3] = '.'
            expanded_graph[y*3+1][x*3+1] = 'F'
            expanded_graph[y*3+1][x*3+2] = 'F'
            expanded_graph[y*3+2][x*3] = '.'
            expanded_graph[y*3+2][x*3+1] = 'F'
            expanded_graph[y*3+2][x*3+2] = '.'
        elif cell == 'L':
            expanded_graph[y*3][x*3] = '.'
            expanded_graph[y*3][x*3+1] = 'L'
            expanded_graph[y*3][x*3+2] = '.'
            expanded_graph[y*3+1][x*3] = '.'
            expanded_graph[y*3+1][x*3+1] = 'L'
            expanded_graph[y*3+1][x*3+2] = 'L'
            expanded_graph[y*3+2][x*3] = '.'
            expanded_graph[y*3+2][x*3+1] = '.'
            expanded_graph[y*3+2][x*3+2] = '.'
        elif cell == 'J':
            expanded_graph[y*3][x*3] = '.'
            expanded_graph[y*3][x*3+1] = 'J'
            expanded_graph[y*3][x*3+2] = '.'
            expanded_graph[y*3+1][x*3] = 'J'
            expanded_graph[y*3+1][x*3+1] = 'J'
            expanded_graph[y*3+1][x*3+2] = '.'
            expanded_graph[y*3+2][x*3] = '.'
            expanded_graph[y*3+2][x*3+1] = '.'
            expanded_graph[y*3+2][x*3+2] = '.'
        elif cell == '7':
            expanded_graph[y*3][x*3] = '.'
            expanded_graph[y*3][x*3+1] = '.'
            expanded_graph[y*3][x*3+2] = '.'
            expanded_graph[y*3+1][x*3] = '7'
            expanded_graph[y*3+1][x*3+1] = '7'
            expanded_graph[y*3+1][x*3+2] = '.'
            expanded_graph[y*3+2][x*3] = '.'
            expanded_graph[y*3+2][x*3+1] = '7'
            expanded_graph[y*3+2][x*3+2] = '.'
        elif cell == 'S':
            expanded_graph[y*3][x*3] = 'S'
            expanded_graph[y*3][x*3+1] = 'S'
            expanded_graph[y*3][x*3+2] = 'S'
            expanded_graph[y*3+1][x*3] = 'S'
            expanded_graph[y*3+1][x*3+1] = 'S'
            expanded_graph[y*3+1][x*3+2] = 'S'
            expanded_graph[y*3+2][x*3] = 'S'
            expanded_graph[y*3+2][x*3+1] = 'S'
            expanded_graph[y*3+2][x*3+2] = 'S'

expanded_graph[0][0] = ''
empty_found = True

while empty_found:
    empty_found = False
    change_count = 0
    for y in range(len(expanded_graph)):
        for x in range(len(expanded_graph[0])):
            if expanded_graph[y][x] == '.' and '' in neighbors(expanded_graph, x, y).values():
                expanded_graph[y][x] = ''
                empty_found = True
                change_count += 1
    print(f"Loop Done: {change_count}")

value = len([cell for row in new_graph for cell in row if cell == '.' ])
print(f"{day_var} - part 2: {value}")
