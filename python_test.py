# test script for Game of Life with python
# much of what is functional from this script will be applicable for Arduino

# import numpy
# import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# declare global variables
N = 100 # size of square grid
ON = 1
OFF = 0
# make game grid
VALS =[ON,OFF]
GAME_GRID = np.random.choice(VALS,N*N,p=[0.2,0.8]).reshape(N,N)

def check_neighbors(grid_row,grid_col,grid):
    neighbor_count = (grid[grid_row, (grid_col-1)%N] + grid[grid_row, (grid_col+1)%N] +
               grid[(grid_row-1)%N, grid_col] + grid[(grid_row+1)%N, grid_col] +
               grid[(grid_row-1)%N, (grid_col-1)%N] + grid[(grid_row-1)%N, (grid_col+1)%N] +
               grid[(grid_row+1)%N, (grid_col-1)%N] + grid[(grid_row+1)%N, (grid_col+1)%N])
    # neighbor_count = 0
    # for row in range(grid_row-1,grid_row+1):
    #     for col in range(grid_col-1,grid_col+1):
    #         if row == grid_row and col == grid_col:
    #             continue
    #         neighbor_count += grid[row%N,col%N]
    return neighbor_count

def set_cell_status(data):
    global GAME_GRID
    new_grid = GAME_GRID.copy()

    for i in range(N):
        for j in range(N):
            neighbor_sum = check_neighbors(i,j,GAME_GRID)

            if GAME_GRID[i,j] == ON:
                if (neighbor_sum < 2) or (neighbor_sum > 3):
                    new_grid[i,j] = OFF
            else:
                if neighbor_sum == 3:
                    new_grid[i,j] = ON

    GAME_GRID = new_grid
    matrix.set_data(GAME_GRID)
    return matrix

fig, axes = plt.subplots()
matrix = axes.matshow(GAME_GRID)
anim = animation.FuncAnimation(fig, set_cell_status, interval=50, save_count=50)
plt.show()
