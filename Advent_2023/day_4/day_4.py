
import os
import re
# import advent_helpers

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
test_data = False
puzzle_input = open(f"{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{day_var}/{day_var}_data.txt").readlines()


def parse_num_list(num_list):
    list_num = {int(num) for num in num_list.split()}
    return list_num


# Part1
total_points = 0
for card in puzzle_input:
    _, card = card.split(':')
    winning_numbers_string, game_numbers_sting = card.split('|')
    winning_numbers = parse_num_list(winning_numbers_string)
    game_numbers = parse_num_list(game_numbers_sting.strip())
    number_intersection = game_numbers.intersection(winning_numbers)

    if len(number_intersection):
        points = 2 ** (len(number_intersection)-1)
        total_points += points

print(f"{day_var} - part 1: {total_points}")

# Part 2
card_list = [1 for i in range(len(puzzle_input))]
for card in puzzle_input:
    card_str, card = card.split(':')
    winning_numbers_string, game_numbers_sting = card.split('|')
    winning_numbers = parse_num_list(winning_numbers_string)
    game_numbers = parse_num_list(game_numbers_sting.strip())
    number_intersection = game_numbers.intersection(winning_numbers)

    if len(number_intersection):
        card_num = int(card_str.strip('Card '))
        for count in range(len(number_intersection)):
            card_list[card_num + count] += card_list[card_num-1]

print(f"{day_var} - part 2: {sum(card_list)}")
