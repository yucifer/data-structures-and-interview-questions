directions = [[-1,0], [0,1], [1,0], [0,-1]]





# Time Complexity : O(N)
# Space Complexity : O(N)

  


def traversalBFS(matrix):
  seen = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
  # print(seen)
  values = []
  queue = [[0,0]]
  while(len(queue)):
    currentPos = queue.pop(0)
    row = currentPos[0]
    col = currentPos[1]
    if (row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col] == True):
      continue
    seen[row][col] = True
    values.append(matrix[row][col])
    for i in range(len(directions)):
      currentDir = directions[i]
      queue.append([row+currentDir[0], col+currentDir[1]])

  return values
  




matrix = [[1+i+5*j for i in range(5)] for j in range(4)]
# print(matrix)
print(traversalBFS(matrix))