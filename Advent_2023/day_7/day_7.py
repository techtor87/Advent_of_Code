
import os
import re
import sys

sys.path.append('../Advent of Code')
from advent_helpers import neighbors

# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = False
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read()
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()


class CamelCardHand():

    def __init__(self, input_str, wild=False):
        self.cards, bid = input_str.strip().split(" ")
        self.bid = int(bid)

        card_dict = {card: self.cards.count(card) for card in set(self.cards)}
        if wild:
            self.card_value = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
            jokers = card_dict.get('J') or 0
            if jokers:
                card_dict.pop('J')
            card_count = sorted(list(card_dict.values()))
            if len(card_count) > 0:
                card_count[-1] += jokers
            else:
                card_count.append(jokers)
        else:
            self.card_value = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
            card_count = sorted(list(card_dict.values()))
        """
        Hand Values:
        1 = Five of a Kind
        2 - Four of a Kind
        3 - Full House (three of a Kind and a Pair)
        4 - Three of a Kind
        5 - Two Pair
        6 - Single Pair
        7 - High Card
        """
        if card_count[-1] == 5:
            self.hand = 1
        elif card_count[-1] == 4:
            self.hand = 2
        elif card_count[-1] == 3 and card_count[-2] == 2:
            self.hand = 3
        elif card_count[-1] == 3:
            self.hand = 4
        elif card_count[-1] == 2 and card_count[-2] == 2:
            self.hand = 5
        elif card_count[-1] == 2:
            self.hand = 6
        else:
            self.hand = 7

    def __lt__(self, other):
        if self.hand == other.hand:
            for s, o in zip(self.cards, other.cards):
                if self.card_value.index(s) == self.card_value.index(o):
                    continue
                return self.card_value.index(s) < self.card_value.index(o)
        else:
            return self.hand < other.hand


# Part1
camel_card_hands = []
for line in puzzle_input:
    camel_card_hands.append(CamelCardHand(line))

camel_card_hands.sort(reverse=True)

scores = [hand.bid*(index+1) for index, hand in enumerate(camel_card_hands)]
print(f"{day_var} - part 1: {sum(scores)}")

# Part 2
camel_card_hands = []
for line in puzzle_input:
    camel_card_hands.append(CamelCardHand(line, wild=True))

camel_card_hands.sort(reverse=True)

scores = [hand.bid*(index+1) for index, hand in enumerate(camel_card_hands)]
print(f"{day_var} - part 2: {sum(scores)}")
