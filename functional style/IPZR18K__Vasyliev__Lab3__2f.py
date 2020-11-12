
def meetUser():
    print("This program help you find the maximum element of the array(array type n*n ) and its index")
    print("limit for n:  1 >= n <= 5")
    return 1

def sizeMatrix(n):
    if (n >= 1 and n <= 5):
        return n
    else:
        print("limit for n:  1 >= n <= 5")
        return 1

def inputMatrix(sizeMatrix, matrix=[], arr=[], i=0, j=0):
    if i == sizeMatrix:
        return matrix
    else:
        if j == sizeMatrix:
            matrix.append(arr)
            arr = []
            return inputMatrix(sizeMatrix, matrix, arr, i + 1, j=0)
        else:
            num = int(input(f"Input value for element matrix [row: {i} column: {j}]: "))
            arr.append(num)
    return inputMatrix(sizeMatrix, matrix, arr, i, j + 1)

def outputMatrix(matrix, sizeMatrix, i=0, j=0, stop=''):
    if i == sizeMatrix:
        return stop
    else:
        if j < sizeMatrix:
            print(matrix[i][j], end=' ')
            return outputMatrix(matrix, sizeMatrix, i, j + 1)
        else:
            print()
            return outputMatrix(matrix, sizeMatrix, i + 1, j=0)

def findMax(matrix, sizeMatrix, maxElem=0, maxRow=0, maxColumn=0, i=0, j=0):
    if i == sizeMatrix:
        return maxElem, maxRow, maxColumn
    else:
        if j == sizeMatrix:
            return findMax(matrix, sizeMatrix, maxElem, maxRow, maxColumn, i + 1, j=0)
        else:
            if matrix[i][j] > maxElem:
                maxElem = matrix[i][j]
                maxRow = i
                maxColumn = j
            return findMax(matrix, sizeMatrix, maxElem, maxRow, maxColumn, i, j + 1)

meetUser()
size = sizeMatrix(int(input("enter your n: \n")))
matrix = inputMatrix(size)
maxElemIndex, maxRowIndex, maxColumnIndex = findMax(matrix, size)
print(f"\nMax element: {matrix[maxRowIndex][maxColumnIndex]}. His row index: {maxRowIndex} column index: {maxColumnIndex}")
