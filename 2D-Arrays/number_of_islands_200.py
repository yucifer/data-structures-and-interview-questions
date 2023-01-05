
# LEETCODE 200
# T : O(M x N)
# S : O(max(N,M))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1,0], [0,1], [1,0],[0,-1]]

        if len(grid) == 0:
            return 0
        islandCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islandCount += 1
                    grid[row][col] = '0'
                    queue = []
                    queue.append([row,col])
                    while(len(queue)):
                        currentPos = queue.pop(0)
                        currentRow = currentPos[0]
                        currentCol = currentPos[1]
                        for i in range(len(directions)):
                            currentDir = directions[i]
                            nextRow = currentRow + currentDir[0]
                            nextCol = currentCol + currentDir[1]
                            if (nextRow < 0 or nextRow >= len(grid) or nextCol < 0 or nextCol >= len(grid[0])):
                                continue
                            if grid[nextRow][nextCol] == '1':
                                queue.append([nextRow, nextCol])
                                grid[nextRow][nextCol] = '0'

        return islandCount