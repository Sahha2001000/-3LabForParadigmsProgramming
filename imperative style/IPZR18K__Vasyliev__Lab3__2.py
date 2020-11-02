print("This program help you find the maximum element of the array(array type n*n ) and its index")
print("limit for n:  1 >= n <= 5")

n = int(input("enter your n: "))

if (n >= 1 and n <= 5):
    arrSize = n * n
    indexMax = arrSize-1
    arr = []
    for i in range(0, arrSize):
        numArr = int(input(f"enter your num for element under the index {i}: "))
        arr.append(numArr)
    for i in range(0, arrSize - 1):
        for j in range(0, arrSize - i - 1):
            if arr[j] > arr[j + 1]:
                indexMax = j
    print(f"\nYour array which you inputted {arr}\n")
    print(f"Max element: {arr[indexMax]}\nYour array under the index: {indexMax} ")
else:
    print("limit for n:  1 >= n <= 5")
