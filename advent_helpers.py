import re
import os
# import networkx as nx

from functools import wraps
import time


def get_xy(x, y):
    pass


def neighbors(grid, x_pos, y_pos):
    # Assumes
    # pos_1 pos_2 pos_3
    # pos_4 pos_5 pos_6
    # pos_7 pos_8 pos_9

    pos_1 = grid[y_pos-1][x_pos-1] if x_pos > 0 and y_pos > 0 else None
    pos_2 = grid[y_pos-1][x_pos] if y_pos > 0 else None
    pos_3 = grid[y_pos-1][x_pos+1] if x_pos < len(grid[0]) - 1 and y_pos > 0 else None
    pos_4 = grid[y_pos][x_pos-1] if x_pos > 0 else None
    pos_5 = grid[y_pos][x_pos]  # current position for refreence
    pos_6 = grid[y_pos][x_pos+1] if x_pos < len(grid[0]) - 1 else None
    pos_7 = grid[y_pos+1][x_pos-1] if x_pos > 0 and y_pos < len(grid) - 1 else None
    pos_8 = grid[y_pos+1][x_pos] if y_pos < len(grid) - 1 else None
    pos_9 = grid[y_pos+1][x_pos+1] if x_pos < len(grid[0]) - 1 and y_pos < len(grid) - 1 else None
    return {'1': pos_1, '2': pos_2, '3': pos_3,
            '4': pos_4, '5': pos_5, '6': pos_6,
            '7': pos_7, '8': pos_8, '9': pos_9}


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time

        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.8f} seconds')
        return result
    return timeit_wrapper
