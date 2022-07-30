## A recursive function to compute a factorial of an integer
num = int(input("Enter an integer: "))

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n

print(factorial(num))