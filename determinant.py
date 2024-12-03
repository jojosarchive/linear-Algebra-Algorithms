import numpy as np


def matrixCreation(rowSize, columnSize):
    matrixSize = rowSize * columnSize
    matrix = np.zeros(matrixSize).reshape(rowSize, columnSize)
    return matrix


matrix1 = matrixCreation(4, 4)


pivots = len(matrix1[0, :])

matrix1[0] = 4

matrix1[0] = matrix1[0] / 2


# pivot 1
# matrix1[0, 0] = 1
# matrix1[0 + 1, 0] = 8

# pivot 2
# matrix1[1, 1] = 2
# matrix1[1 + 1, 1] = 8

# pivot 3
# matrix1[2, 2] = 3
# matrix1[2 + 1, 2] = 8

# pivot 4
# matrix1[3, 3] = 4
# matrix1[3, 3] = 8


print(matrix1)