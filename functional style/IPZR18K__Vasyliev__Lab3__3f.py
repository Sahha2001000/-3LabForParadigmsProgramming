def meetUser():
    print("This program help revers array which you inputted")
    return 1

def inptArr(i, sizeArr, arr):
    if i == sizeArr:
        return arr
    num = int(input(f"enter your num for element under the index {i}: "))
    arr.append(num)
    return inptArr(i + 1, sizeArr, arr)

def sizeArr():
    sizeArr=int(input("Enter size array: "))
    return sizeArr

def arrRevers(i, sizeArr, arr, arrRev):
    if i == -(sizeArr)-1:
        return arrRev
    arrRev.append(arr[i])
    return arrRevers(i - 1, sizeArr, arr, arrRev)


meetUser()

arr =[]
size = sizeArr()
inptArr(0, size, arr)

arrRev = []
arrRevers(-1, size, arr, arrRev)

print(f"\nYour array: {arr}")
print(f"\nYour array reverse: {arrRev}")
