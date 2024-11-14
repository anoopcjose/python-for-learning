
class NumberChecker:
    def __init__(self):
        self.num1 = int(input("Enter your number"))

    def check_even_or_odd(self):
        if self.num1 % 2 == 0:
            print("Number is even")
        else:
            print("Number is odd")




number = NumberChecker()
number.check_even_or_odd()

number1 = NumberChecker()
number1.check_even_or_odd()