def largest(numbers):
    if len(numbers) == 0:
        return "List is empty"

    big = numbers[0]

    for i in numbers:
        if i > big:
            big = i

    return big

numbers = [10, 45, 25, 80, 35]

result = largest(numbers)
print("Largest number:", result)
