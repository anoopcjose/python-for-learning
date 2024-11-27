# num = int(input())
# for number in range(num):
#     num = num + number
# print(num)




class group:
    def __init__(self):
        self.num = int(input())
    def sequence(self):
        for number in range(self.num):
            self.num = self.num + number
        print(self.num)
num1 = group()
num1.sequence()