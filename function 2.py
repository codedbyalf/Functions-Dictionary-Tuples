def sumlist(numbers):
    total = 0

    for i in numbers:
        total = total + 1

    return total

numbers = [10, 20, 30, 40, 50]

result = sumlist(numbers)
print("Sum of numbers: ", result)
