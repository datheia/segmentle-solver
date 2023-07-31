import itertools
import numpy as np

def solve_grid(input_grid, target):
    flat_list = [item for sublist in input_grid for item in sublist]
    all_perms = list(itertools.permutations(flat_list, len(flat_list)))
    for perm in all_perms:
        grid = np.array(perm).reshape(-1, len(input_grid[0])).tolist()
        if all(sum(column) == target for column in zip(*grid)):
            return grid
    return False

grid = [[7, 2, 6], [5, 4, 12], [15, 14, 7]]
target = 24

print(solve_grid(grid, target))
