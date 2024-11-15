# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# number * range(1,11) = result
number = int(input())

for item in range(1,11):
    result = number * item
    print(f"{number} x {item} = {number * item}")
