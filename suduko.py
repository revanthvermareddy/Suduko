#code
import numpy as np
board = np.array([
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
    ])

def print_board(bo):
    for i in range(len(bo)):
        if(i%3==0 and i!=0):
            print("---------------------")
        for j in range(len(bo[i])):
            if(j%3==0 and j!=0):
                print("|", end=' ')
            if(j==8):
                print(bo[i][j])
            else:
                print(bo[i][j], end=' ')

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if (bo[i][j]==0):
                return (i, j)
    return None
    
def valid(bo, val, pos):
    
    # checking row #1
    # for i in range(len(bo)):
    #     if val == bo[pos[0]][i] and pos[1] != i:
    #         # print(val,' exists in row')
    #         return False
    
    # checking row #2
    if val in bo[pos[0]]:
        return False
    
    # checking column #1
    # for i in range(len(bo)):
    #     if val == bo[i][pos[1]] and pos[0] != i:
    #         # print(val, ' exists in column')
    #         return False
    
    # checking column #2
    # for i in range(len(bo)):
    #     if val == bo[i][pos[1]]:
    #         return False
    
    # checking column #3
    if val in bo.T[pos[1]]:
        return False
            
    box_x = pos[0] // 3 # floor division
    box_y = pos[1] // 3 # floor division
    
    # checking box #1
    # for i in range(box_x*3, box_x*3 + 3):
    #     for j in range(box_y*3, box_y*3 + 3):
    #         if(val == bo[i][j]) and (i,j)!= pos:
    #             return False
    
    # checking box #2
    if val in board[box_x*3:box_x*3+3, box_y*3:box_y*3+3]:
        return False

    return True

def solve(bo):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
   
    for num in range(1,10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num
            
            if solve(board):
                return True
            
            bo[row][col] = 0 # imp step for back tracking
    
    return False

print('Initial Board :')
print_board(board)

solve(board)

print('\n\nSolved Board :')
print_board(board)