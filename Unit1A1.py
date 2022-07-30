# import factorial from math, will be used to determine if factors of num are prime
from math import factorial

# ask for integer input
num = int(input("Enter an integer: "))

# get all factors of num and add to list num_factors
num_factors = []

for i in range(2, int(num / 2) + 1):
    if (num % i) == 0:
        num_factors.append(i)
    else:
        continue

# check all values in num_factors to see if they are prime
# if they are, add to list prime_factors
unique_prime_factors = []

for n in num_factors:
    if (factorial(n - 1) % n == n - 1):
        unique_prime_factors.append(n)
    else:
        continue

# print unique_prime_factors list
print(unique_prime_factors)