print("This program will help you check if you are entering a prime or non-prime number")
num = int(input("Enter you num: "))
div = 2
while num % div != 0 and  num  > 1:
    res = num // div
    div += 1
if num == div:
    print(f"Your number is prime: {num}")
else:
    res = num / div
    print(f"You number is not prime: {num} / {div} = {res}")
