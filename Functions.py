# def say_hello():
#     print("Hello")
#
#
# say_hello()
# say_hello()
# say_hello()
from random import choice


# def say_hello(): print("Hello")


# def say_hello():
#     print("Hello")
#
#
# def say_goodbye():
#     print("Good Bye")
#
#
# say_hello()
# say_goodbye()


# def print_messages():
#     def say_hello(): print("Hello")
#     def say_goodbye(): print("Good Bye")
#     say_hello()
#     say_goodbye()
#
# print_messages()


# def main():
#     say_hello()
#     say_goodbye()
#
# def say_hello(): print("Hello")
# def say_goodbye(): print("Good Bye")
#
# main()







# ПАРАМЕТРЫ ФУНКЦИИ

# def say_hello(name):
#     print(f"Hello {name}")
#
# say_hello("Tom")
# say_hello("Bob")
# say_hello("Alice")


# def print_person(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#
# print_person("Tom", 37)

# def say_hello(name = "Tom"):
#     print(f"Hello {name}")
#
# say_hello()
# say_hello("Bob")


# def print_person(name, age = 18):
#     print(f"Name: {name} age: {age}")
#
# print_person("Bob")
# print_person("Tom", 37)


# def print_person(name = "Tom", age = 18):
#     print(f"Name {name} Age {age}")
#
# print_person()
# print_person("Bob")
# print_person("Sam", 37)


# def print_person(name, age):
#     print(f"Name {name} Age {age}")
#
# print_person(age=22, name="Tom")


# def print_person(name, *, age, company):
#     print(f"Name: {name} Age: {age}, Company: {company}")
#
# print_person("Bob", age = 21, company = "Microsoft")


# def print_person(*, name, age, company):
#     print(f"Name: {name}, Age: {age}, Company: {company}")
#
# print_person(name = "Tom", age= 36, company= "Microsoft" )


# def print_person(name, /, age, company):
#     print(f"Name: {name}, Age: {age}, Company: {company}")
#
# print_person("Bob", age = 56, company= "Microsoft")


# def print_person(name, /, age = 18, *, company):
#     print(f"Name : {name}, Age: {age}, Company: {company}")
#
# print_person("Tom", company="Microsoft")
# print_person("Tom", 37, company= "Microsoft")
# print_person("Bob", company= "Microsoft", age= 21)


# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(f"Sum = {result}")
#
# sum(1, 2, 3, 4 ,5)
# sum(3,4,5,6)










# ОПЕРАТОР RETURN И ВОЗВРАЩЕНИЕ РЕЗУЛЬТАТА ИЗ ФУНКЦИИ

# def get_message():
#     return "Hello METANIT.COM"
#
# message = get_message()
# print(message)


# def double(number):
#     return 2 * number
#
# result1 = double(5)
# result2 = double(4)
# print(f"Result1 = {result1}")
# print(f"Result2 = {result2}")

# def sum(a, b):
#     return a + b
#
# result = sum(4, 6)
# print(f"sum(4, 6) = {result}")
# print(f"sum(3, 5) = {sum(3, 5)}")


# def print_person(name, age):
#     if age > 120 or age < 1:
#         print("Invalid age")
#         return
#     print(f"Name: {name} Age: {age}")
#
# print_person("Tom", 48)
# print_person("Bob", 156)









# ФУНКЦИЯ КАК ТИП, ПАРАМЕТР И РЕЗУЛЬТАТ ДРУГОЙ ФУНКЦИИ

# def say_hello(): print("Hello")
# def say_goodbye(): print("Good Bye")
#
# message = say_hello
# message()
# message = say_goodbye
# message()


# def sum(a, b): return a + b
# def multiply(a, b): return  a * b
#
# operation = sum
# result = operation(5, 6)
# print(result)
#
# operation = multiply
# print(operation(8, 10))


# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"Result = {result}")
#
# def sum(a, b): return a + b
# def multiply(a, b): return  a * b
#
# do_operation(5,4,sum)
# do_operation(5,4,multiply)


# def sum(a,b): return a + b
# def subtract(a,b): return  a - b
# def multiply(a,b): return  a * b
#
# def select_operation(choice):
#     if choice == 1:
#         return sum
#     elif choice == 2:
#         return subtract
#     else:
#         return  multiply
#
# operation = select_operation(1)
# print(operation(10,6))
#
# operation = select_operation(2)
# print(operation(4,7))
#
# operation = select_operation(3)
# print(operation(5,6))









# ЛЯМБДА-ВЫРАЖЕНИЯ

# message = lambda: print("hello")
#
# message()

# square = lambda  n: n * n
#
# print(square(4))
# print(square(5))

# def do_operation(a,b,operation):
#     result = operation(a,b)
#     print(f"result = {result}")
#
# do_operation(5,4,lambda a,b: a + b)
# do_operation(5,4,lambda a,b: a * b)

# def select_operation(choice):
#     if choice == 1:
#         return lambda a, b: a + b
#     elif choice == 2:
#         return lambda a, b: a - b
#     else:
#         return lambda a, b: a * b
#
# operation = select_operation(1)
# print(operation(6,9))
#
# operation = select_operation(2)
# print(operation(4,7))
#
# operation = select_operation(3)
# print(operation(1,2))



# ____________________________________________________________________________________________________________________
#
# # Напиши функцию, которая принимает два числа и возвращает их сумму. Вызови её с разными значениями.
# def fnk(a, b):
#     result = a + b
#     print(result)
#
# fnk(int(input("Введите число1: ")), int(input("Введите число1: ")))
#
# # Создай функцию, которая принимает два числа и возвращает большее из них.
# def fnk(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
#
# fnk(int(input("Введите число1: ")), int(input("Введите число1: ")))
#
# # Напиши функцию, которая принимает строку и число nn, и возвращает строку, повторённую nn раз.
# def fnk(lst, n):
#         lst *= n
#         print(lst)
#
# lst = ["hello"]
# fnk(lst, 3)
#
# # Реализуй функцию, которая проверяет, является ли переданное число чётным.
# def fnk(a):
#     if a % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
# fnk(int(input("Введите число: ")))
#
# # Создай функцию, которая принимает список чисел и возвращает сумму всех элементов списка.
# def fnk(lst):
#     result = sum(lst)
#     print(result)
#
# lst = [1,2,3,4,5,6,7,8,9]
# fnk(lst)
#
# # Напиши функцию, которая возвращает факториал числа, используя цикл.
# def fnk(n):
#     a = 0
#     b = 1
#     while a < n:
#         a += 1
#         b *= a
#     print(b)

# def fnc(n):
#     a = 1
#     for i in range(1, n+1):
#         a *= (i)
#     return a
#
# print(fnc(5))


#
# fnk(int(input("Введите число: ")))
#
# # Создай функцию, которая принимает число и возвращает количество цифр в нём.
# def fnk(n):
#     a = []
#     while n > 0:
#         a.append(n % 10)
#         n //= 10
#     print(len(a))
#
# fnk(int(input("Введите число: ")))

# def fnc(a):
#     b = 0
#     while a > 0:
#         b += 1
#         a //= 10
#     return b
#
# print(fnc(694721))



#
# # Реализуй функцию, которая находит максимальную цифру в числе.
# def fnk(n):
#     d_max = 0
#     while n > 0:
#         d = n % 10
#         if d > d_max:
#             d_max = d
#         n //= 10
#     print(d_max)
#
# fnk(int(input("Введите число: ")))
#
# # Напиши функцию, которая проверяет, является ли строка палиндромом (читается одинаково с обеих сторон).
# def fnc(strn):
#     lst = []
#     for i in strn:
#         lst.append(i)
#     a = len(lst)
#     b1 = 0
#     b2 = a - 1
#     while b1 < b2:
#         if lst[b1] != lst[b2]:
#             print("Не Палиндром")
#             return
#         else:
#             b1 += 1
#             b2 -= 1
#     print("Палиндром")
#
# fnc(input("Введите текст: "))

# def fnc(a):
#     if a == a[::-1]:
#         print("Палиндром")
#     else:
#         print("Не Палиндром")
#
# fnc(input("Введите текст: "))


#
# # Создай функцию, которая принимает два числа и возвращает их НОД (наибольший общий делитель).
# def fnc(a, b):
#     d = ()
#     if a % b != 0:
#         lst1 = []
#         while d != 0:
#             d = a % b
#             lst1.append(d)
#             a = b
#             b = d
#         print(lst1[-2])
#     else:
#         lst1 = []
#         while d != 0:
#             d = b % a
#             lst1.append(d)
#             b = a
#             a = d
#         print(lst1[-2])
#
#
# fnc(int(input("Введите число1: ")), int(input("Введите число2: ")))

# def fnc(a, b):
#     while b != 0:
#         a, b = b, a % b
#     print(a)
#
# fnc(int(input("Введите число1: ")), int(input("Введите число2: ")))

#
# # Напиши функцию, которая принимает два числа. Если их сумма больше 100, верни True, иначе — False.
# def fnc(a, b):
#     d = a + b
#     if d > 100:
#         return True
#     else:
#        return False
#
# print(fnc(int(input("Введите число1: ")), int(input("Введите число2: "))))
#
# # Создай функцию, которая принимает строку и возвращает её длину.
# def fnc(str):
#     lst = []
#     for i in str:
#         lst.append(i)
#     return len(lst)
#
# print(fnc(input("Введите текст: ")))
#
# # Реализуй функцию, которая принимает список чисел и возвращает количество чётных и нечётных чисел в виде кортежа.
# def fnc(lst):
#     s1 = 0
#     s2 = 0
#     for i in lst:
#         if i % 2 != 0:
#             s2 += 1
#         else:
#             s1 += 1
#     return (s1, s2)
#
#
# lst = [25, 58, 59]
# result = fnc(lst)
# print(result)
#
# # Напиши функцию, которая принимает три числа и возвращает их среднее арифметическое.
# def fnc(n1, n2, n3):
#     return (n1 + n2 + n3) / 3
#
#
# print(fnc(int(input("Введите число1: ")), int(input("Введите число2: ")), int(input("Введите число3: "))))
#
# # Создай функцию, которая принимает список чисел и возвращает новый список, где все элементы увеличены на 5.
# def fnc(num):
#     a = []
#     for i in num:
#         a.append(i + 5)
#     return a
#
#
# num = [6, 9, 4, 7, 2, 1, 12, 749, 69]
# print(fnc(num))
#
# # Создай две функции: первая вычисляет площадь прямоугольника,
# # вторая принимает длину и ширину и возвращает сообщение о площади, вызывая первую функцию.
# def fnc1(a, b): return  a * b
#
# def fnc2(length, width):
#     a = length
#     b = width
#     print(fnc1(a, b))
#
# fnc2(6, 9)
#
# # Реализуй функцию, которая принимает список строк и возвращает список их длин.
# def fnc1(nstr):
#     a = []
#     for i in nstr:
#         a.append(len(i))
#     return a
#
# def fnc2(strk):
#         print(fnc1(strk))
#
# strk = ["fsgfg", "fgdf", "rwtrgk"]
# fnc2(strk)
#
# # Напиши функцию, которая принимает строку и возвращает её зеркальное отражение (например, "abc" → "cba").
# def fnc1(a):
#     b = "".join(reversed(a))
#     return b
#
# def fnc(a):
#     print(fnc1(a))
#
# a = "abc"
# fnc(a)
#
# # Создай функцию, которая принимает два числа и выполняет операцию
# # (сложение, вычитание, умножение или деление) в зависимости от переданного имени операции.
# def sum(a, b): return  a + b
# def subtract(a, b): return  a - b
# def multiply(a, b): return  a * b
# def divide(a, b): return  a / b
#
# def select(a, b, choice):
#     if choice == "+":
#         return (sum(a,b))
#     elif choice == "-":
#         return (subtract(a, b))
#     elif choice == "*":
#         return (multiply(a, b))
#     else:
#         return (divide(a ,b))
#
# a = int(input("Введите число1: "))
# b = int(input("Введите число2: "))
# choice = input("Введите знак: ")
#
# print(select(a, b, choice))
#
# # Напиши функцию, которая вызывает другую функцию для проверки, является ли число простым.
# def fnc1(a):
#     if a <= 1:
#         print("Число не является простым")
#     else:
#         for i in range(2, a // 2 + 1):
#             if a % i == 0:
#                 print("Число не является простым")
#                 break
#         else:
#             print("Число простое")
#
# def fnc(a):
#     fnc1(a)
#
# fnc(int(input("Введите число: ")))
#
#
# # Создай функцию, которая принимает список чисел и функцию.
# #  Она должна возвращать новый список, элементы которого обработаны переданной функцией.
# def fnc(a, b, oper):
#     result = oper(a, b)
#     print(result)
#
# def mult(a, b):
#     d = []
#     for i in a:
#         d.append(i * b)
#     return d
#
# fnc([4, 9, 6], 2, mult)
#
# # Реализуй функцию, которая принимает две функции и число. Она возвращает результат сложения их результатов, вызванных с этим числом.
# def fnk(a, oper1, oper2):
#     result = oper1(a) + oper2(a)
#     print(result)
#
# def sq(a):
#     return a ** 2
#
# def mult(a):
#     return  a * 2
#
# fnk(3, sq, mult)
#
# # Напиши функцию, которая принимает два числа и функцию. Если функция возвращает True, выведи их сумму, иначе — разность.
# def fnc(a, b, oper):
#     if oper(a, b) is True:
#         result = a + b
#     else:
#         result = a - b
#     print(result)
#
# def fnc2(a, b):
#     if a < b:
#         return True
#     else:
#         return False
#
# fnc(9, 6, fnc2)
#
#
# # Напиши лямбда-функцию, которая принимает число и возвращает его квадрат. Вызови её с разными значениями.
# sq = lambda a: a * a
#
# print(sq(int(input("Введите число: "))))
#
# # Создай список чисел и с помощью функции filter и лямбда-выражения оставь только чётные числа.
# even = lambda n: n % 2 == 0
# num = [1,2,3,4,5,6,7,8,9]
#
# result = filter(even, num)
# print(list(result))


















