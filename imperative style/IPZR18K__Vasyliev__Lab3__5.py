print("This program transform from your decimal number to hexadecimal number.")
numDec = int(input("Enter your decimal number: "))
num = numDec
numHexList = []
hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

while numDec > 0:
    numHexList.append(hex[numDec % 16])
    numDec = numDec // 16

sizeList = -len(numHexList) - 1
hexNumList = []
for i in range(-1, sizeList, -1):
    tmp = numHexList[i]
    hexNumList.append(str(tmp))

numHex = "".join(hexNumList)
print(f"From decimal number: {num} to hexadecimal number: {numHex}")

