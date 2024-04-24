
import os
import re
# import advent_helpers

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
test_data = False
puzzle_input = open(f"{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{day_var}/{day_var}_data.txt").readlines()


def get_rgb(input):
    if red_search := re.search(r'(\d*) red', input):
        red = int(red_search.group(1))
    else:
        red = 0

    if green_search := re.search(r'(\d*) green', input):
        green = int(green_search.group(1))
    else:
        green = 0

    if blue_search := re.search(r'(\d*) blue', input):
        blue = int(blue_search.group(1))
    else:
        blue = 0

    return red, green, blue


max_value = {'red': 12, 'green': 13, 'blue': 14}
# Part1
id_sum = 0
for game in puzzle_input:
    game_id, games = game.split(':')
    game_possible = True
    for game in games.strip().split(';'):
        red_count, green_count, blue_count = get_rgb(game)
        if red_count > max_value['red'] or green_count > max_value['green'] or blue_count > max_value['blue']:
            game_possible = False
            break

    if game_possible:
        id_sum += int(game_id.strip('Game '))

print(f"{day_var} - part 1: {id_sum}")

# Part 2
id_sum = 0
for game in puzzle_input:
    game_id, games = game.split(':')
    red_max = green_max = blue_max = 0
    for game in games.strip().split(';'):
        red_count, green_count, blue_count = get_rgb(game)
        if red_count > red_max:
            red_max = red_count

        if green_count > green_max:
            green_max = green_count
        if blue_count > blue_max:
            blue_max = blue_count

    id_sum += red_max * green_max * blue_max
print(f"{day_var} - part 2: {id_sum}")
