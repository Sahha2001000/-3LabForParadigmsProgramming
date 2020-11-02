def meetUser():
    print("This program will help you check if you are entering a prime or non-prime number")

def isPrime(num, div=2):
    if num % div != 0 and num > 1:
        div += 1
        if num == div:
            return num
        return isPrime(num, div + 1)
    else:
        return div

def outputProgram(num, div):
    if num == div:
        print(f"Your number is prime: {num}")
    else:
        res = num / div
        print(f"You number is not prime: {num} / {div} = {res}")


meetUser()
num = int(input("Enter you num: "))
res = isPrime(num)
res = outputProgram(num, res)
