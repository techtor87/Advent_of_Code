
import os
import re
import sys

sys.path.append('../Advent of Code')
from advent_helpers import neighbors


def LNDS(s):
    start = 0
    cur_len = 1
    max_len = 1
    for i in range(1,len(s)):
        if ord(s[i]) in (ord(s[i-1]), ord(s[i-1])+1):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
                start = i - cur_len
            cur_len = 1
    if cur_len > max_len:
        max_len = cur_len
        start = len(s) - cur_len
    return s[start:start+max_len]


def check_password(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    if not (matches := re.match(r'(\w)\1(?!\1.*)(\w(?!\1))\2', password)):
        if len(matches.group(1)) > 2 or len(matches.group(3)) > 2:
            return False
        return False
    if len(LNDS(password)) < 3:
        return False

    return True


def increment_password(password):
    password_list = list(password)
    for pos in range(7, -1, -1):
        password_list[pos] = chr(ord(password[pos])+1)
        if password_list[pos] == '{':
            if pos != 0:
                password_list[pos-1] = chr(ord(password[pos-1])+1)
                password_list[pos] = 'a'
            else:   # pos == 0
                return 'aaaaaaaa'
        else:
            break
    return ''.join(password_list)


# Setup Data
day_var = os.path.basename(os.path.dirname(__file__))
year_var = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
test_data = True
puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").read().strip() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").read().strip()
# puzzle_input = open(f"{year_var}/{day_var}/{day_var}_test_data.txt").readlines() if test_data else open(f"{year_var}/{day_var}/{day_var}_data.txt").readlines()

password = increment_password(puzzle_input)
# Part1
while not check_password(password):
    password = increment_password(password)

# removed_disallowed_substrings = [string.strip() for string in puzzle_input if not re.search(r'(ab|cd|pq|xy)', string)]
# ensure_double_substring = [string for string in removed_disallowed_substrings if re.search(r'(\w)\1', string)]
# ensure_enough_vowels = [string for string in ensure_double_substring if len(''.join(re.findall(r'[aeiou]', string))) >= 3]

print(f"{day_var} - part 1: {password}")

# Part 2



value = 0
print(f"{day_var} - part 2: {value}")
