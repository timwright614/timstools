import numpy as np

def sq_address(x):
    return (x[0]//3*3+x[1]//3,x[0]%3*3+x[1]%3)

def trans(x):
    return np.array(x).T.tolist()

def available_ints(x,grid, grid_trans, grid_squares):
    j = x[0]
    i = x[1]
    total = []
    total.extend(grid[j])
    total.extend(grid_trans[i])
    total.extend(grid_squares[sq_address(x)[0]])
    available = [x for x in range(1,10) if x not in total]
    return available

def update(x, val, grid, grid_trans, grid_squares):
    j = x[0]
    i = x[1]
    grid[j][i] = val
    grid_trans[i][j] = val
    y = sq_address(x)
    grid_squares[y[0]][y[1]] = val

def sudoku_solver(grid):


    grid_trans = trans(grid)
    grid_squares = [[0 for i in range(9)] for i in range(9)]
    for j in range(9):
        for i in range(9):
            x = sq_address((j,i))
            grid_squares[x[0]][x[1]] = grid[j][i]

    emptys = []
    for j in range(9):
        for i in range(9):
            if grid[j][i] == 0:
                emptys.append([(j,i),[]])


    while any(0 in i for i in grid):

        for index, element in enumerate(emptys):
            if element[1] == []:
                if available_ints(element[0],grid, grid_trans, grid_squares) != []:
                    element[1] = available_ints(element[0],grid, grid_trans, grid_squares)
                    update(element[0],element[1][0], grid, grid_trans, grid_squares)
                    break

                else:
                    for i in emptys[::-1]:
                        if len(i[1]) == 1:
                            i[1].pop(0)
                            update(i[0],0, grid, grid_trans, grid_squares)
                        if len(i[1]) > 1:
                            i[1].pop(0)
                            update(i[0],i[1][0], grid, grid_trans, grid_squares)
                            break
                    break

    return grid
