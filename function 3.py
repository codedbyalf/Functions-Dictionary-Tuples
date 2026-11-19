def multiply_list(numbers):
    result = 1

    for i in numbers:
        result = result * i

    return result

numbers = [2, 3, 4, 5]

answer = multiply_list(numbers)
print("Product of numbers: ", answer)
