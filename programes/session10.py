# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# number * range(1,11) = result
class MultiplicationTable:
    def __init__(self):
        self.number = int(input())

    def multiplication(self):
        for item in range(1, 11):
            print(f"{self.number} x {item} = {self.number * item}")



multiplicant = MultiplicationTable()
multiplicant.multiplication()