# i refer to row index and j refers to column index
import numpy as np
#expected output
# 3 prints 

if __name__ == "__main__":
  #1. Print a specific 3x3 matrix where a cell is 1 if i == j, else 0 
  #self note: can also use np.eye(3)
  firstMatrix = np.array([[0,0,0],[0,0,0],[0,0,0]])
  for i in 0, 1, 2:
    for j in 0, 1, 2:
      if(i == j):
        firstMatrix[i][j] += 1
  
  for row in firstMatrix:
    print(" ".join(map(str,row)))

  #2. Print the 3x3 matrix from #1 and then add 3 to every cell where i ≠j  
  secondMatrix = firstMatrix
  for i in 0, 1, 2:
    for j in 0, 1, 2:
      if(i != j):
        secondMatrix[i][j] += 3
  
  print("\n")

  for row in secondMatrix:
    print(" ".join(map(str,row)))
  
  print("\n")

  #3. Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created 
  thirdMatrix = np.delete(secondMatrix, 2, 1)
  for row in thirdMatrix:
    print(" ".join(map(str,row)))