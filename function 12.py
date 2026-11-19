def palindrome(string):
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

string = input("Enter a string: ")

palindrome(string)
