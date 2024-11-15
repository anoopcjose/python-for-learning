numbers = [12, 32, 43, 3, 5, 46, 46, 24.34, 54]
class odd_or_even_list:
    def __init__(self,numbers):
        self.numbers = numbers

    def is_even(self,number):
        if number % 2 == 0:
            return True
        else:
            return False

    def printer_o_e(self):
        for number in self.numbers:
            if self.is_even(number) == True:
                print("even number")
            else:
                print("number is odd")

o_e_calculation = odd_or_even_list(numbers)
o_e_calculation.printer_o_e()