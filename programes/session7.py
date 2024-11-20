class NumberChecker:
    def __init__(self):
        self.x = int(input("Enter a number: "))

    def check_even_odd(self):
        if self.x % 2 == 0:
            print(f'{self.x} is even')
        else:
            print(f'{self.x} is odd')

num = NumberChecker()
num.check_even_odd()


number = -5

if number > 0:
    print('Positive number')

elif number < 0:
    print('Negative number')

else:
    print('Zero')

print('This statement is always executed')

