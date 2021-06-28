'''
image is N x N matrix, each pixel represented by an integer. Rotate image 90 degrees

'''

def rotate90Clockwise(matrix) :
  if (len(matrix) == 0):
    return False
  n = len(matrix)
  for layer in range(n // 2):
    first, last = layer, n - layer - 1
    for i in range(first, last):
      # save top
      top = matrix[layer][i]

      # left -> top
      matrix[layer][i] = matrix[-i - 1][layer]

      # bottom -> left
      matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

      # right -> bottom
      matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

      # top -> right
      matrix[i][-layer - 1] = top
  return matrix

def solveCounterClockwise(matrix):
  if not matrix or not matrix[0]:
    return []
  n = len(matrix)
  for row in matrix:
    row.reverse()
  for i in range(n):
    for j in range(i):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  return matrix

def rotate2(matrix):
  n = len(matrix)
  result = [[0] * n for i in range(n)]
  for i,j in zip(range(n), range(n - 1, -1, -1)):
    for k in range(n):
      result[k][i] = matrix[j][k]
    return result
  
A = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

print(A)

# print(rotate90Clockwise(A))
print(solveCounterClockwise(A))