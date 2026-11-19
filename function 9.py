def prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if prime(num):
    print("Number is Prime")
else:
    print("Number is not Prime")
