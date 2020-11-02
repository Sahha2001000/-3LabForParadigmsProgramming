def meetUser():
    print("This program transform from your decimal number to hexadecimal number.")
    return 1

def arrRevers(arr_1, arr_2, i=-1):
    size = -(len(arr_1)) - 1
    if i == size:
        return arr_2
    arr_2.append(str(arr_1[i]))
    return arrRevers(arr_1, arr_2, i - 1)

def ListToStr(arr):
    strArr = ''.join(arr)
    return strArr


def DecToHex(numDec, arr, hex, arrHex):
    if numDec == 0:
        return ListToStr(arrRevers(arr, arrHex))
    else:
        arr.append(hex[numDec % 16])
        return DecToHex(numDec // 16, arr, hex, arrHex)


def outputNum(numDec, numHex):
    print(f"From decimal number: {numDec} to hexadecimal number: {numHex}")
    return 1


def hexList():
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    return hex


meetUser()
hex = hexList()
numDec = int(input("Enter your decimal number: "))
num = numDec

arr = []
arrHex = []

numHex = DecToHex(numDec, arr, hex, arrHex)
outputNum(num,numHex)
