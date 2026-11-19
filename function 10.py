def even_numbers(t):
    for i in t:
        if i % 2 == 0:
            print(i)

t = (10, 15, 20, 25, 30, 35, 40)

print("Even numbers are: ")
even_numbers(t)
