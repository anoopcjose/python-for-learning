def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 5
print("The factorial of", num, "is", factorial(num))

# 5! = 5 x 4 x 3 x 2 x 1 = 120
# x = 5
# 5 x factorial(4)
# x = 4
# 4 x factorial(3)
# x = 3
# 3 x factorial(2)
# x = 2
# 2 x factorial(1)
# x = 1
# return 1






# Ans = 120
# x = 5
# 5 x 24
# x = 4
# 4 x 6
# x = 3
# 3 x 2
# x = 2
# 2 x 1
# x = 1
# return 1