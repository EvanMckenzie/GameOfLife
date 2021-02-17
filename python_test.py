# test script for Game of Life with python
# much of what is functional from this script will be applicable for Arduino

# import numpy
# import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# declare global variables
N = 10 # size of square grid
ON = 1
OFF = 0

# define dictionary to reference RGB values for colors that will be assigned to cells
COLOR_DICT = {
    "red": [255,0,0],
    "orange": [255,125,0],
    "yellow": [255,255,0],
    "sea_green": [125,255,0],
    "green": [0,255,0],
    "turquoise": [0,255,125],
    "cyan": [0,255,255],
    "ocean": [0,125,255],
    "blue": [0,0,255],
    "violet": [125,0,255],
    "magenta": [255,0,255],
    "raspberry": [255,0,125]
}

# make game grid
VALS =[ON,OFF]
COLORS = ["red","orange","yellow","sea_green","green","turquoise","cyan","ocean","blue","violet","magenta","raspberry"]
GAME_GRID = []
for i in range(N):
    for j in range(N):
        GAME_GRID.append([int(np.random.choice(VALS,1,p=[0.2,0.8])),str(np.random.choice(COLORS,1))])
#GAME_GRID = np.random.choice(VALS,N*N,p=[0.2,0.8]).reshape(N,N)
print(GAME_GRID)


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
