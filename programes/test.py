class NumberComparer:
	def __init__(self):
		self.y = int(input("Enter your number"))
		self.x = int(input("Enter your number"))
	def compare(self):
		if self.x == self.y:
			print(self.x, ' and ', self.y, ' are equal')
		else :
			if self.x > self.y:
				print(self.x, ' is greater than ', self.y)
			else :
				print(self.x, ' is less than ', self.y)

			
comparer = NumberComparer()
comparer.compare()