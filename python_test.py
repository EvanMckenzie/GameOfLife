# test script for Game of Life with python
# much of what is functional from this script will likely be applicable for Arduino

# import numpy
# import matplotlib
import numpy as np
import matplotlib as plt

# Generate matrix of 1 and 0 (100x100)
game_grid = np.random.randint(2, size=(10,10))

# initialize num_row and num_col variables
game_grid_size = game_grid.shape()

num_row = game_grid_size[0]
num_col = game_grid_size[1]

# initialize count for neighboring cells
neighbor_count = 0

# for loops to index into matrix
for i in range(num_row):
    for j in range(num_col):
        for row in range(i-1,i+1):
            for col in range(j-1,j+1):
                if (row == i) and (col == j):
                    pass
                neighbor_count += game_grid[row%num_row,col%num_col]
                if game_grid[i,j] == 1:
                    if neighbor_count == 2 or neighbor_count == 3:
                        game_grid[i,j] = 1
                    else:
                        game_grid[i,j] = 0
                elif game_grid[i,j] = 0:
                    if neighbor_count == 3:
                        game_grid[i,j] = 1
