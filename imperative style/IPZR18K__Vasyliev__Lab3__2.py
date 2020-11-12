print("This program help you find the maximum element of the matrix(matrix type n*n ) and it's index (row and column)")
print("limit for n:  1 >= n <= 5")
n = int(input("enter your n: "))
if (n >= 1 and n <= 5):
    i = 0
    j = 0
    matrix = []
    # create matrix n*n
    # row
    for i in range(0, n):
        # arr for user nums
        arr = []
        # column
        for j in range(0, n):
            num = int(input(f"Input value for element matrix [row: {i} column: {j}]: "))
            arr.append(num)
        matrix.append(arr)

    # output user's matrix
    print(f"\nYour matrix which you inputted (type {n} * {n}): ")
    for i in range(0, n):
        for j in range(0, n):
            print(matrix[i][j], end=' ')
        print()

    # find max matrix element  and his index column and row
    maxElem = 0
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] > maxElem:
                maxRowIndex = i
                maxColumnIndex = j
                maxElem = matrix[i][j]

    print(f"\nMax element: {matrix[maxRowIndex][maxColumnIndex]}. His row index: {maxRowIndex} column index: {maxColumnIndex}")
else:
    print("limit for n:  1 >= n <= 5")
