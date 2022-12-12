def factorial(num):
    #creates function
    x = 1
    #makes variable x = 1
    for i in range(1, num + 1):
        x *= i
    return x

print(factorial(5))
