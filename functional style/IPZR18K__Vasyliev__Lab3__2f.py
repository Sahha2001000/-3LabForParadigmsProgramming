def meetUser():
    print("This program help you find the maximum element of the array(array type n*n ) and its index")
    print("limit for n:  1 >= n <= 5\n")
    return 1

def sizeArr(n):
    if (n >= 1 and n <= 5):
        n = n * n
        return n
    else:
        print("limit for n:  1 >= n <= 5\n")
        return 1


def maxIndex(arr, sizeArr):
    if sizeArr == 0:
        return 0
    else:
        i = maxIndex(arr, sizeArr - 1)
        if arr[i] > arr[sizeArr - 1]:
            return i
        return sizeArr - 1


def inptArr(i, sizeArr, arr):
    if i == sizeArr:
        return arr
    k = int(input(f"nenter your num for element under the index {i}: "))
    arr.append(k)
    return inptArr(i + 1, sizeArr, arr)


def outputMaxArr(indexMax, arr):
    print(f"\nMax element: {arr[indexMax]}\nYour array under the index: {indexMax} ")
    return 1


meetUser()

arr = []
size = int(input("enter your n: "))
size = sizeArr(size)

arr = inptArr(0, size, arr)

indexMax = maxIndex(arr, size)

outputMaxArr(indexMax, arr)
