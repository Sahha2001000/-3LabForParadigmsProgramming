print("This program help find factorial your number which  you enter")
n = int(input("Enter your n: "))
k=n
fact = 1
while (n >= 1):
    fact = fact * n
    n -= 1
print(f"Factorial number {k}  : {fact}")
