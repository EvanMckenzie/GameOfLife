# test script for Game of Life with python
# much of what is functional from this script will likely be applicable for Arduino

# import numpy
# import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# declare global variables
N = 10 # size of square grid

def check_neighbors(grid_row,grid_col):
    for row in range(grid_row-1,grid_row+1):
        for col in range(grid_col-1,grid_col+1):
            if row == grid_row and col == grid_col:
                continue
            neighbor_count += game_grid[row%N,col%N]
    return neighbor_count

def set_cell_status():
    for i in range(N):
        for j in range(N):
            neighbor_sum = check_neighbors(i,j)

            if game_grid[i,j] == 1:
                if neighbor_sum == 2 or neighbor_sum == 3:
                    game_grid[i,j] = 1
                else:
                    game_grid[i,j] = 0
            elif game_grid[i,j] == 0:
                if neighbor_sum == 3:
                    game_grid[i,j] = 1

def animate_grid(grid):
    # ANIMATION USING MATPLOTLIB --TO BE UPDATED--
    fig, ax = plt.subplots()
    mat = ax.matshow(grid)
    ani = animation.FuncAnimation(fig, update, interval=50,
                                  save_count=50)
    plt.show()

def main():
    try:
        # make game grid
        game_grid=[]
        game_grid = np.random.choice(game_grid,N*N,p=[0.2,0.8]).reshape(N,N)

        #put into while loop to have run until user cancels it
        while True:
            # call set_cell_status to get into grid
            set_cell_status()
            # call animate_grid to make it run
            animate_grid(game_grid)
    except KeyboardInterrupt:
        pass
