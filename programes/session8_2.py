# Write a program that takes a number as input and checks if it is a multiple of both 3 and 7.
# num = int(input("Write a number"))
#
#  if num % 3 == 0 and num % 7 == 0 :
#      print("Multiple of 3 and 7")
#  else:
#      print("Not a Multiple of 3 and 7")

class MultipleGroup:
    def __init__(self):
        self.num = int(input("Write a number"))
    def Multiple_of_3_and_7(self):
        if self.num % 3 == 0 and self.num % 7 == 0:
            print("Multiple of 3 and 7")
        else:
            print("Not a Multiple of 3 and 7")
number = MultipleGroup()
number.Multiple_of_3_and_7()
