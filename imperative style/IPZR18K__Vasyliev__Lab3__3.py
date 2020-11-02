print("This program help revers array which you inputted")
sizeArr=int(input("Enter size array: "))

arr = []
for i in range(0,sizeArr):
    num = int(input(f"\nenter your num for element under the index {i}: "))
    arr.append(num)
print(f"Your array: {arr}")

arrRevers=[]
sizeArrRev = -(len(arr))-1
for i in range(-1,sizeArrRev,-1):
    element = arr[i]
    arrRevers.append(element)
    
print(f"\nYour array reverse: {arrRevers}")
