def count_letters(string):
    upper = 0
    lower = 0

    for i in string:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1

    print("Uppercase letters: ", upper)
    print("Lowercase letters: ", lower)

string = input("Enter a string: ")

count_letters(string)
