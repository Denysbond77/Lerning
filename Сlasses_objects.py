# class Person:
#     pass
#
# tom = Person()
# bob = Person()


# class Person:
#     def __init__(self):
#         print("Создание объекта Person")
#
# tom = Person()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# tom = Person("Tom", 44)
#
# print(tom.name)
# print(tom.age)
#
# tom.age = 47
# print(tom.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# tom = Person("Tom", 44)
# bob = Person("Bob", 45)
#
# print(tom.name)
# print(bob.name)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# tom = Person("Tom", 44)
#
# tom.company = "Microsoft"
# print(tom.company)


# class Person():
#     def say_hello(self):
#         print("Hello")
#
# tom = Person()
# tom.say_hello()


# class Person():
#     def say(self, message):
#         print(message)
#
# tom = Person()
# tom.say("Hello METANIT.COM")


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print(f"Name: {self.name} Age: {self.age}")
#
# tom = Person("Tom", 22)
# tom.display_info()
#
# bob = Person("Bob", 45)
# bob.display_info()


# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("Создан человек с именем", self.name)
#
#     def __del__(self):
#         print("Удален человек с именем", self.name)
#
# tom = Person("Tom")


# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("Создан человек с именем", self.name)
#
#     def __del__(self):
#         print("Удален человек с именем", self.name)
#
# def create_person():
#     tom = Person("Tom")
#
# create_person()
# print("Конец программы")

# _______________________________________________________________________________________________________________

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def display_info(self):
#         print(f"Название: {self.title}Автор: {self.author} Год издания: {self.year}")
#
# kobzar = Book("Kobzar ", "Shevchenko ", 1860 )
# kobzar.display_info()


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         print(self.width * self.height)
#
#     def perimeter(self):
#         print(self.width*2 + self.height*2)
#
# rect = Rectangle(6, 9)
# rect.area()
# rect.perimeter()


# class Car:
#     def __init__(self, brand, model, year, mileage):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self. mileage = mileage
#
#     def drive(self, x):
#         print(self.mileage + x)
#
#     def get_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}")
#
# SEAT = Car("SEAT", "Cordoba", 2007, 180)
# SEAT.drive(10)
# SEAT.get_info()


# class Calculator:
#     def __init__(self):
#         pass
#
#     def add(self, a, b):
#         print(a + b)
#
#     def subtract(self, a, b):
#         print(a - b)
#
#     def multiply(self, a, b):
#         print(a * b)
#
#     def divide(self, a, b):
#         if b == 0:
#             print("error")
#         else:
#             print(a / b)
#
# calc = Calculator()
#
# calc.add(6, 9)
# calc.subtract(4, 7)
# calc.multiply(2, 2)
# calc.divide(4, 6)


# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = []
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def average(self):
#         if not self.grades:
#             average = 0
#         else:
#             average = sum(self.grades) / len(self.grades)
#         return average
#
# tom = Student("Tom", 20, [])
# tom.add_grade(100)
# tom.add_grade(80)
# tom.add_grade(90)
# print(tom.average())

















