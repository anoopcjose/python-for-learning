# numbers  = [1,27,44,35,5,66,93,85,74]
# largest = 0
# # for number in numbers:
# #     if number > largest:
# #         largest = number
# #
# # print(largest)




numbers  = [1,27,44,35,5,66,94,85,174]
largest = 0

class group:
    def __init__(self,numbers,largest):
        self.largest = largest
        self.numbers = numbers
    def largest_finder(self):
        for number in self.numbers:
            if number > self.largest:
                self.largest = number
        print(self.largest)


num1 = group(numbers,largest)
num1.largest_finder()

