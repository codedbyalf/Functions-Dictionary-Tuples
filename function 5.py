def factorial(n):
    if n < 0:
        return "Factorial is not defined"

    fact = 1

    for i in range(1, n+1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))

result = factorial(n)
print("Factorial is: ", result)
