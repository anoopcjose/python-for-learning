num = int(input("Write a number"))

if num == 0:
    print("0 is not positive or negative")
    num = num * 0
    print(num)
else:
    if num > 0:
        print("Number is Positive")
        num = num * 1
        print(num)
    else:
        print("Number is negative")
        num = num * 1
        print(num)
