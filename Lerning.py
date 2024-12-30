# print(2+3)
# print("Hello")
from tomllib import TOMLDecodeError

# if 1 < 2:
#     print("Hello")

# print("Hello Python")
#
# print("Full name:", "Tom", "Smith")

# name = input("Введите имя:")
# print("Привет!" ,name,)

# name = "Tom"
# print(name)

# name = "Tom"
# print(name)
# name= "Bob"
# print(name)

# isMarried = False
# print(isMarried)
#
# isAlive = True
# print(isAlive)

# age = 21
# print("Возраст", age)
#
# count = 15
# print("Количество", count)

# a = 0b11
# b = 0b1011
# c = 0b100001
# print(a)
# print(b)
# print(c)

# a = 0o7
# b = 0o11
# c = 0o17
# print(a)
# print(b)
# print(c)

# a = 0x0A
# b = 0xFF
# c = 0xA1
# print(a)
# print(b)
# print(c)

# height = 1.68
# pi = 3.14
# weight = 68.
# print(height)
# print(pi)
# print(weight)

# x = 3.9e3
# print(x)

# x = 3.9e-3
# print(x)

# text = ("Laudate omnes gentes laudate "
#         "Magnificat in secula")
# print(text)

# text = '''Laudate omnes gentes laudate
# Magnificat in secula
# Et anima mea laudate
# Magnificat in secula '''
# print(text)

# text = "Message:\n\"Hello World\""
# print(text)

# path = r"C:\python\name.txt"
# print(path)

# userName = "Tom"
# userAge = 37
# user = f"name: {userName} age: {userAge}"
# print(user)

# userID = "abc"
# print(userID)
#
# userID = 234
# print(userID)

# userID = "abc"
# print(type(userID))
#
# userID = 234
# print(type(userID))

# print("Hello World", end = " ")
# print("Hello METANIT.COM", end = ": ")
# print("Hello python", end = " ")

# name = input("Введите ваше имя: ")
# print(f"Ваше имя: {name}")

# name = input("Your name: ")
# age = input("Your age: ")
# print(f"Your name: {name} Your age: {age}")

# print(6-2)
# print(6+2)
# print(6*2)
# print(6/2)
# print(7/2)
# print(7//2)
# print(7**2)
# print(7%2)

# import keyword
#
# # Выводим список ключевых слов
# print(keyword.kwlist)

# number = 3+4*5**2+7
# print(number)
#
# number = (3+4)*(5**2+7)
# print(number)

# number = 10
# number +=5
# print(number)
# number-=3
# print(number)
# number*=4
# print(number)

# first_number = 2.0001
# second_number = 5
# third_number = first_number/second_number
# print(third_number)
#
# print(2.0001 + 0.1)

# first_number = 2.0001
# second_number = 0.1
# third_number = first_number + second_number
# print(round(third_number, 4))

# print(round(2.51))
# print(round(2.49))
#
# print(round(3.5))
# print(round(2.5))

# print(round(2.554, 2))
# print(round(2.555, 2))
# print(round(2.565, 2))
# print(round(2.575, 2))
# print(round(2.655, 2))
# print(round(2.5551, 2))
# print(round(2.55499999, 2))
# print(round(2.499, 2))

# number = 6
# print(f"number = {number:0b}")

# number = 0b101
# print(f"number = {number:0b}")
# print(f"number = {number}")

# x1 = 2
# y1 = 5
# z1 = x1 & y1
# print(f"z1 = {z1}")

# x2 = 4
# y2 = 5
# z2 = x2 & y2
# print(f"z2 = {z2:0b}")
# print(f"z2 = {z2}")

# x2 = 4
# y2 = 5
# z2 = x2 | y2
# print(f"z2 = {z2:0b}")
# print(f"z2 = {z2}")

# x2 = 9
# y2 = 5
# z2 = x2 ^ y2
# print(f"z2 = {z2:0b}")
# print(f"z2 = {z2}")

# x = 36
# key = 30
#
# encrypt = x ^ key
# print(f"Зашифрованное число: {encrypt:0b}")
# print(f"Зашифрованное число: {encrypt}")
#
# decrypt = encrypt ^ key
# print(f"Расшифрованное число: {decrypt:0b}")
# print(f"Расшифрованное число: {decrypt}")

# x = 6
# print(f"x = {x:0b}")
# y = 9
# print(f"y = {y:0b}")
# x = x ^ y
# print(f"x = {x}")
# print(f"y = {y}")
# print(f"x = {x:0b}")
# print(f"y = {y:0b}")
# y = x ^ y
# print(f"x = {x}")
# print(f"y = {y}")
# print(f"x = {x:0b}")
# print(f"y = {y:0b}")
# x = x ^ y
# print(f"x = {x}")
# print(f"y = {y}")
# print(f"x = {x:0b}")
# print(f"y = {y:0b}")
#
# print(f"x = {x}")
# print(f"y = {y}")

# x = 5
# y = ~x
#
# print(f"y: = {y}")

# a = 5
# print(f"a = {a:0b}")
# b = 1
# print(f"b = {b:0b}")
# c = a << b
# print(c)
#
# d = a >> b
# print(d)

# name = "Denys"
# age = 47
# print(f"Меня зовут {name} мне {age} лет")

# name = input("Имя: ")
# number = input("Число: ")
# print(f"{name}, твоё любимое число - {number}")

# n1 = int(input("число 1: "))
# n2 = int(input("число 2: "))
# sum = n1 + n2
# dif = n1 - n2
# pro = n1 * n2
# div_ord = n1 / n2
# div_int = n1 // n2
# print(f"Сумма: {sum}")
# print(f"Разность: {dif}")
# print(f"Произведение: {pro}")
# print(f"Обычное деление: {div_ord}")
# print(f"Целочисленное деление: {div_int}")

# n1 = int(input("число 1: "))
# n2 = int(input("число 2: "))
# div_rem = n1 % n2
# print(f"Остаток деления: {div_rem}")

# n = int(input("число: "))
# d = int(input("степень: "))
# deg = n**d
# print(f"Результат: {deg}")

# n = int(input("число: "))
# x = n << 1
# print(f"Результат: {x}")

# n = int(input("число: "))
# x = n >> 2
# print(f"Результат: {x}")

# n1 = int(input("число1: "))
# n2 = int(input("число2: "))
# x = n1 & n2
# print(f"Результат: {x:0b}")


# n = int(input("число: "))
# print(f"{n:0b}")

# n = int(input("число: "))
# print(f"Двоичное представление: {n:0b}")

# n = int(input("число: "))
# binary_rep = bin(n)
# print(f"Двоичное представление: {binary}")

# text = input("Введите строку: ")
# point = input("Введите разделитель: ")
# print(text.split(point))

print(18 % 24)
















