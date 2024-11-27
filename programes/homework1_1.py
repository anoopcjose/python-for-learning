
# num = input()
# if num == num[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


class group:
    def __init__(self):
        self.num = input()
    def palindrome(self):
        if self.num == self.num[::-1]:
            print("palindrome")
        else:
            print("not palindrome")
num1 = group()
num1.palindrome()