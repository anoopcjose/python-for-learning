def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

numbers = [12,32,43,3,5,46,46,24.34,54]
for number in numbers:
    if is_even(number) == True:
        print("even number")
    else:
        print("number is odd")
