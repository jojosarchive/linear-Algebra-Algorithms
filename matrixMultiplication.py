import numpy as np
import random


# helper functions to make matrices
def matrixCreation(rowSize, columnSize):
    matrixSize = rowSize * columnSize
    matrix = np.zeros(matrixSize).reshape(rowSize, columnSize)
    return matrix


def matrixPopulation(matrix):
    rowSize = range(len(matrix[0, :]))
    columnSize = range(len(matrix[:, 0]))

    for i in rowSize:
        for j in columnSize:
            matrix[i, j] = random.randint(1, 15)


# helper function for algorithm
# takes the dot product of two vectors
def dotProduct(row, column):
    product = 0
    for i in range(len(row)):
        product = product + row[i] * column[i]
    return product


# user input for the rows and columns of the two matrices being multiplied
mat1Rows = int(input("Enter amount of rows for matrix 1\n"))
mat1Cols = int(input("Enter amount of columns for matrix 1\n"))
mat2Rows = int(input("Enter amount of rows for matrix 2\n"))
mat2Cols = int(input("Enter amount of columns for matrix 2\n"))

# logic check to see if these two matrices can be multiplied
# matrix 1 = nxm and matrix 2 = kxp, if m = k then it can be multiplied
if mat1Cols != mat2Rows:
    raise ValueError("Matrices cannot be multiplied")

# creation of the two matrices
matrix1 = matrixCreation(mat1Rows, mat1Cols)
matrix2 = matrixCreation(mat2Rows, mat2Cols)
matrixPopulation(matrix1)
matrixPopulation(matrix2)

# creation of the matrix that will represent the product
matrix3 = matrixCreation(mat1Rows, mat2Cols)

# matrix multiplication algorithm

# iterates through each row
for rows in range(mat1Rows):
    # iterates through each column
    for columns in range(mat2Cols):
        # creates an element of the matrix
        matrix3[rows, columns] = dotProduct(matrix1[rows, :], matrix2[:, columns])

print(f"Matrix 1\n{matrix1}\n")
print(f"Matrix 2\n{matrix2}\n")
print(f"Matrix 3 (Product)\n{matrix3}\n")