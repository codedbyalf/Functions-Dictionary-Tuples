def perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    if num > 0 and total == num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

num = int(input("Enter a number: "))

perfect(num)
