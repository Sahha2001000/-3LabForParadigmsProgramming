def meetUser():
    print("This program help find factorial your number which  you enter")
    return 1

def factorialFind(n):
    if (n == 0):
        return 1
    return n * factorialFind(n - 1)

meetUser()
n = int(input("Enter your n: "))
num = n
result = factorialFind(n)
print(f"Factorial number {n}  : {result}")

