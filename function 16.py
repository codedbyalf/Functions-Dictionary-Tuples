def calculation(a, b):
    add = a + b
    sub = a - b

    return add, sub

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

addition, subtraction = calculation(x, y)

print("Addition:", addition)
print("Subtraction:", subtraction)
