
# num = input()
# if num == num[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


class group:
    def __init__(self,num):
        self.num = str(num)
    def palindrome(self):
        if self.num == self.num[::-1]:
            print("palindrome")
        else:
            print("not palindrome")
num = int(input())
num1 = group(num)
num1.palindrome()