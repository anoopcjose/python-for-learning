class Multiple5:
    def __init__(self, number_list):
        self.number_list = number_list

    def print_multiple_of_5(self):
        [print(number, "is multiple of 5") for number in self.number_list if number % 5 == 0]



numbers = [10, 20, 33, 46, 55]
num = Multiple5(numbers)
num.print_multiple_of_5()