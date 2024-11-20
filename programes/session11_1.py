# 0,1,1,2,3,5,8,13,21,34...
number1 = 0
number2 = 1
length = 10
print(number1)
print(number2)
for item in range(10):
    num = number1 + number2
    print(num)
    number1 = number2
    number2 = num




# 0th = 0
# 1st = 1
# 2nd = 0th + 1st
# 3rd = 1st + 2nd

