
# LEETCODE 286 Walls and Gates
# T : O(N)
# S : O(N)

WALL = -1
GATE = 0
EMPTY = 2147483647

directions = [[-1,0], [0,1], [1,0], [0,-1]]

def wallsAndGates(matrix):
    def dfs(matrix, row, col, currentStep):
        if (row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] < currentStep):
            return 
        matrix[row][col] = currentStep
        for i in range(len(directions)):
            currentDir = directions[i]
            dfs(matrix, row+currentDir[0], col+currentDir[1], currentStep+1)



    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == GATE:
                dfs(matrix, row, col, 0)

    return matrix


print(wallsAndGates([[EMPTY, -1, 0, EMPTY ], [EMPTY, EMPTY, EMPTY, -1], [EMPTY, -1, EMPTY, -1], [0, -1, EMPTY, EMPTY]]))
