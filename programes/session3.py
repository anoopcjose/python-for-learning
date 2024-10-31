class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John", 25)
print("Name:", person1.name)
print("Age:", person1.age)



class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog1 = Dog("Buddy", "Labrador")
print(dog1.name)
print(dog1.breed)