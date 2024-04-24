from itertools import zip_longest
from functools import cmp_to_key


def compare_pair(left, right):
    if type(left) is int and type(right) is int:
        if left <= right:
            return True
        else:
            return False
    elif type(left) is list and type(right) is list:
        sub_bool = True
        for l, r in zip_longest(left, right):
            if l == None:
                return sub_bool
            if r == None:
                return False
            sub_bool &= compare_pair(l, r)
        return sub_bool
    elif type(left) is int and type(right) is list:
        return compare_pair([left], right)
    elif type(left) is list and type(right) is int:
        return compare_pair(left, [right])
    else:
        print(f"Unknown Compare: {left} --- {right}")


def compare(left, right):
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for l2, r2 in zip_longest(left, right):
            if (result := compare(l2, r2)) != 0:
                return result
        return 0
    else:
        l2 = [left] if isinstance(left, int) else left
        r2 = [right] if isinstance(right, int) else right
        return compare(l2, r2)


puzzle_input = open("day_13_test_data.txt").read().strip()
pairs = puzzle_input.split("\n\n")

pairs_list = []
for pair in pairs:
    left, right = pair.split("\n")
    pairs_list.append((eval(left), eval(right)))
