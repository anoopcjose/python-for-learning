# 2 - 1,2
# 3 - 1,3
# 5 - 1,5
# 7 - 1,7
# 11- 1,11
# 8 - 1,2,4,8
# 21 - 1,3,7,21
# num = 13
# num % range(2,num) == 0

num = int(input())
for item in range(2,num):
    if num % item == 0:
        print("Not prime")
        break
    else:
        print("prime")
        break