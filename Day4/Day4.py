"""
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.


@ denotes a roll of paper.
a forklift can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions

Sounds like a CNN kernel to me, apply the 3x3 kernel and if value is lower or equal than 4 its considered true. 
"""
import pandas as pd
import numpy as np
from scipy.signal import convolve2d


def load_data(dir):
    with open(dir, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def apply_convolution(grid):

    kernel = np.array([
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ])

    neighbor_count = convolve2d(grid,kernel, mode="same", boundary = "fill", fillvalue = 0)

    accessible = (grid == 1) & (neighbor_count < 4)
    return accessible

def solve_p2(text_data):
    counter = 0
    can_remove = True
    rounds = 0
    grid = np.array([[1 if c == '@' else 0 for c in row] for row in text_data])
    while can_remove:
        accessible = apply_convolution(grid)
        removed_this_round = accessible.sum()
        

        if (removed_this_round == 0):
            can_remove = False
        else:
            grid = np.where(accessible, 0, grid)
            counter += removed_this_round
            rounds += 1
    return counter, rounds, grid

def solve_p1(text_data):
    grid = np.array([[1 if c == '@' else 0 for c in row] for row in text_data])
    accessible = apply_convolution(grid)
    return accessible.sum()


if __name__ == "__main__":

    input_data = load_data("input.txt")
    test_data = load_data("test.txt")

    print(solve_p1(test_data))
    print(solve_p1(input_data))

    removed, rounds, grid = solve_p2(test_data)
    print(f"Removed: {removed}, in {rounds} rounds")
    print("Final Grid: \n" , grid)
    removed, rounds, grid = solve_p2(input_data)
    print(f"Removed: {removed}, in {rounds} rounds")
    print("Final Grid: \n" , grid)
