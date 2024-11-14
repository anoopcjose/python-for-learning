# Write a function to calculate the sum of elements in a list that are greater than a given number.


class SumOfElements:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.num = int(input("Write your number"))
        self.sum = 0
    def number_sum(self):
        for self.number in self.numbers:
            if self.number > self.num:
                self.sum = self.sum + self.number
        print(self.sum)

number_1 = SumOfElements()
number_1.number_sum()