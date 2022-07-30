
# prompt user for phone number
x = int(input("Enter your phone number with no spaces or slashes: "))

sum_of_x = 0
p = x
while p > 0:
    digit = p % 10
    sum_of_x = sum_of_x + digit
    p = p // 10
print(sum_of_x)

y = x - sum_of_x

sum_of_y = 0
while y > 0:
    y_dig = y % 10
    sum_of_y = sum_of_y + y_dig
    y = y // 10
print(sum_of_y)