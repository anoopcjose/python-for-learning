# numbers = [10, 20, 33, 46, 55]
# class Multiple5:
#     def __init__(self,numbers):
#         self.numbers = numbers
#     def Multiple_of_5(self):
#         if self.numbers % 5 == 0 :
#             print("Multiple of 5")
#         else:
#             print("Not a Multiple of 5")
# number = Multiple5(numbers)
# number.Multiple_of_5()
#

numbers = [10, 20, 33, 46, 55]
class Multiple5:
    def __init__(self,numbers):
        self.numbers = numbers

    def is_multiple_of_5(self,number):
        if number % 5 == 0:
            return True
        else:
            return False

    def final_answer(self):
        for number in self.numbers:
            if self.is_multiple_of_5(number) == True:
                print(number," is multiple of 5")
            else:
                print(number ,"is not a multiple of 5")
num = Multiple5(numbers)
num.final_answer()