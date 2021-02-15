# test script for Game of Life with python
# much of what is functional from this script will likely be applicable for Arduino

# import numpy
# import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# declare global variables
N = 10 # size of square grid
ON = 1
OFF = 0
# make game grid
VALS =[ON,OFF]
GAME_GRID = np.random.choice(VALS,N*N,p=[0.2,0.8]).reshape(N,N)

def check_neighbors(grid_row,grid_col,grid):
    neighbor_count = 0
    for row in range(grid_row-1,grid_row+1):
        for col in range(grid_col-1,grid_col+1):
            if row == grid_row and col == grid_col:
                continue
            neighbor_count += grid[row%N,col%N]
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
    mat.set_data(GAME_GRID)
    return mat

fig, ax = plt.subplots()
mat = ax.matshow(GAME_GRID)
ani = animation.FuncAnimation(fig, set_cell_status, interval=50, save_count=50, blit=True)
plt.show()
