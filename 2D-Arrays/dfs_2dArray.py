directions = [[-1,0], [0,1], [1,0], [0,-1]]





# Time Complexity : O(N)
# Space Complexity : O(N)

  
def traversalDFS(matrix):
  seen = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
  # print(seen)
  values = []
  def dfs(matrix, row, col, seen , values):
    if (row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col] == True):
      return
    values.append(matrix[row][col])
    seen[row][col] = True
    for i in range(0, len(directions)):
      currentDir = directions[i]
      dfs(matrix, row+currentDir[0], col+currentDir[1], seen, values)
  
  
  dfs(matrix, 0, 0, seen , values)
  return values


  




matrix = [[1+i+5*j for i in range(5)] for j in range(4)]
# print(matrix)
print(traversalDFS(matrix))