# 2 - 1,2
# 3 - 1,3
# 5 - 1,5
# 7 - 1,7
# 11- 1,11
# 8 - 1,2,4,8
# 12- 1,2,3,4,6,12
# 21 - 1,3,7,21
# num = 13
# num % range(2,num) == 0
num = int(input())
flag = False
for item in range(2,int(num/2)+1):
    if num % item == 0:
        flag = True
        break

if flag == True:
    print("Not Prime")
else:
    print("Prime")
