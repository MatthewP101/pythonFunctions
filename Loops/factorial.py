def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result

print("The factorial of 5 is:")
print(factorial(5))

#factoral just times all numbers below n Eg. 5 would be 5x4x3x2x1 = 120


list = [5,6,7]

for num in list:
    print(f"The factorial of {num} is: {factorial(num)}")