def unique_list(numbers):
    new_list = []

    for i in numbers:
        if i not in new_list:
            new_list.append(i)

    return new_list

numbers = [1, 2, 2, 3, 4, 4, 5]

result = unique_list(numbers)
print("List with distinct elements: ", result)
