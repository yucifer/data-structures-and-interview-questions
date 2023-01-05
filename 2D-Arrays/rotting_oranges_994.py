# LEETCODE 994

# T : O(N)
# S : O(N)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROTTEN = 2
        FRESH = 1
        EMPTY = 0

        directions = [[-1,0], [0,1],[1,0], [0,-1] ]

        queue = []
        freshOrangeCount = 0
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == FRESH:
                    freshOrangeCount += 1
                if grid[row][col] == ROTTEN:
                    queue.append([row,col])

        queueSize = len(queue)
        minutes = 0 
        while(len(queue)):
            if queueSize == 0:
                queueSize = len(queue)
                minutes += 1
            currentOrange = queue.pop(0)
            queueSize -= 1
            for i in range(len(directions)):
                currentDir = directions[i]
                nextRow = currentOrange[0] + currentDir[0] # row
                nextCol = currentOrange[1] + currentDir[1] # col
                if (nextRow < 0 or nextRow >= len(grid) or nextCol < 0 or nextCol >= len(grid[0])):
                    continue
                if grid[nextRow][nextCol] == FRESH:
                    freshOrangeCount -= 1
                    grid[nextRow][nextCol] = ROTTEN
                    queue.append([nextRow, nextCol])
        if freshOrangeCount > 0:
            return - 1
        else:
            return minutes


