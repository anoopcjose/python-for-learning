class Vehicle:
    def __init__(self,Brand):
        self.Brand = Brand
class Car(Vehicle):
    def __init__(self,Brand,Model):
        super().__init__(Brand)
        self.Model = Model
car1 = Car("Honda", "Amaze")
print(car1.Model)
print(car1.Brand)