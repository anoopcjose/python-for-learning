class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John", 25)
print("Name:", person1.name)
print("Age:", person1.age)
person2 = Person(14, "Jack")
print("Name:", person2.name)
print("Age:", person2.age)
print("Name:", person1.name)
print("Age:", person1.age)

# __________________________________________________________________

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

# __________________________________________________________________

name = "Aagney"
print(name)
name = "Jack"
print(name)
print(person1.name)




class Student:
    def __init__(self, student_name):
        self.student_name = student_name
class Result(Student):
    def __init__(self, student_name , exam_mark):
        super().__init__(student_name)
        self.exam_mark = exam_mark
class Set(Result):
    def __init__(self,exam_mark,set):
        super().__init__(exam_mark)
        self.set = set

subjectNamemark = Set(20 , 2)
print(subjectNamemark.exam_mark)
print(subjectNamemark.set)






















