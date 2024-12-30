from http.cookiejar import lwp_cookie_str


# # ПРЕОБРАЗОВАНИЕ ТИПОВ
#
# a = ("2")
# b = 3
# c = int(a) + b
# print(c)


# age = 22
# message = "Age: " + str(age)
# print(message)


# # ОБЛАСТЬ ВИДИМОСТИ ПЕРЕМЕННЫХ
#
# name = "Tom"
#
# def say_hi():
#     print("Hello", name)
#
# def say_bye():
#     print("Good bye", name)
#
# say_hi()
# say_bye


# def say_hi():
#     name = "Sam"
#     surname = "Johnson"
#     print("Hello", name, surname)
#
# def say_bye():
#     name = "Tom"
#     print("Good bye", name)
#
# say_hi()
# say_bye()


# name = "Tom"
#
# def say_hi():
#     name = "Bob"
#     print("Hello", name)
#
# def say_by():
#     print("Good bye", name)
#
# say_hi()
# say_by()


# name = "Tom"
#
# def say_hi():
#     global name
#     name = "Bob"
#     print("Hello", name)
#
# def say_bye():
#     print("Good bye", name)
#
# say_hi()
# say_bye()


# def other():
#     n = 5
#
#     def inner():
#         print(n)
#
#     inner()
#     print(n)
#
# other()


# def other():
#     n = 5
#
#     def inner():
#         n = 25
#         print(n)
#
#     inner()
#     print(n)
#
# other()


# def other():
#     n = 5
#
#     def inner():
#         nonlocal n
#         n = 25
#         print(n)
#
#     inner()
#     print(n)
#
# other()


# ЗАМЫКАНИЯ

# def other():
#     n = 5
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(n)
#
#     return inner
#
# fn = other()
#
# fn()
# fn()
# fn()
# fn()


# def multiply(n):
#     def inner(m): return  n * m
#
#     return inner
#
# fn = multiply(6)
# print(fn(5))
# print(fn(6))
# print(fn(8))


# def multiply(n): return lambda m: m * n
#
# fn = multiply(5)
# print(fn(5))
# print(fn(6))
# print(fn(7))


# ДЕКОРАТОРЫ

# def select(input_func):
#     def output_func():
#         print("****************")
#         input_func()
#         print("****************")
#     return output_func
#
# @select
# def hello():
#     print("Hello METANIT.COM")
#
# hello()


# def check(input_func):
#     def output_func(*args):
#         input_func(*args)
#     return output_func
#
# @check
# def print_person(name, age):
#     print(f"Name: {name}, Age: {age}")
#
# print_person("Tom", 38)


# def check(input_func):
#     def output_func(*args):
#         name = args[0]
#         age = args[1]
#         if age < 0: age = 1
#         input_func(name, age)
#     return output_func
#
# @check
# def print_person(name, age):
#     print(f"Name: {name}, Age: {age}")
#
# print_person("Tom", 38)
# print_person("Bob", -5)


# def check(input_func):
#     def output_func(*args):
#         result = input_func(*args)
#         if result < 0: result = 0
#         return result
#     return output_func
#
# @check
# def sum(a, b):
#     return a + b
#
# result1 = sum(10, 20)
# print(result1)
#
# result2 = sum(10, -20)
# print(result2)

# ______________________________________________________________________________________________________________________

# # Напиши программу, которая запрашивает у пользователя число и выводит его в виде:
# #
# #     Целого числа (int),
# #     Вещественного числа (float),
# #     Строки (str).
#
# n = input("число: ")
#
# print(int(n))
# print(float(n))
# print(str(n))
#
#
# # Создай функцию, которая принимает строку с числом и возвращает сумму его цифр.
# # Например: "12345" → 15.
#
# text = input("")
#
# def fnc(text):
#     num = int(text)
#     num2 = []
#     while num > 0:
#         num2.append(num % 10)
#         num //= 10
#     return sum(num2)
#
# print(fnc(text))



# text = input("")
#
# def fnc(text):
#     return sum(int(i) for i in text if i.isdigit())
#
# print(fnc(text))



# # Напиши функцию, которая принимает список чисел (в строковом виде) и возвращает новый список, где все элементы преобразованы в числа.
#
# num = ["1","2","3","4","5"]
#
# def fnc(num):
#     return [int(i) for i in num]
#
# print(fnc(num))
#
#
#
# # Создай функцию, которая принимает целое число и возвращает его двоичное, восьмеричное и шестнадцатеричное представление.
#
# def fnc(a):
#     bi = bin(a)
#     oc = oct(a)
#     he = hex(a)
#     return (f"бин: {bi}, окт: {oc}, хекс: {he}")
#
# print(fnc(int(input("Введите число: "))))
#
#
# # Напиши программу, которая запрашивает у пользователя строку и проверяет, можно ли её преобразовать в число.
# # Если можно, вывести "Число", иначе "Не число".
#
# text = input("")
#
# if text.replace("-","",1).replace(".","",1).isdigit():
#     print("число")
# else:
#     print("не число")



# Область видимости переменных:
#
#     Создай функцию, в которой объявляется локальная переменная. Попробуй обратиться к этой переменной за пределами функции и объясни результат.
#
# a = 9
#
# def fnc(a):
#     b = 6
#
# d = a + b
# print(d)
#
#     Создай глобальную переменную и напиши функцию, которая её изменяет. Выведи значение переменной до и после вызова функции.
#
# a = 6
# print(a)
#
# def fnc():
#     global a
#     a = 9
#     print(a)
#
# fnc()
#
#
#
#
#     Создай две функции. В одной функции объяви переменную и вызови вторую функцию. Попробуй получить доступ к переменной из второй функции.
#
# def fnc():
#     a = 9
#     def fnc2():
#         nonlocal a
#         a = 4
#     fnc2()
#     print(a)
#
# fnc()
#
#
#     Напиши программу, где используется как глобальная, так и локальная переменная с одинаковым именем. Покажи, как их отличать.
#
# a = 4
#
# def fnc():
#     a = 7
#     return a
#
# print(fnc())
# print(a)
#
#
#     Создай программу с функцией, которая принимает параметр и использует глобальную переменную для вычислений.
#
# a = 2
#
# def fnc(b):
#     return a + b
#
# print(fnc(6))



# Замыкания:
#
#     Напиши функцию, которая возвращает другую функцию. Внешняя функция принимает число n, а внутренняя умножает любое переданное ей число на n.
#     Пример:

# def multiply(n):
#     def inner(m): return  m * n
#     return inner
#
# fnc = multiply(6)
# print(fnc(9))

# multiply_by_3 = outer_function(3)
# print(multiply_by_3(5))  # 15
#
#     Создай функцию, которая принимает строку и возвращает функцию, добавляющую к этой строке новый текст.
#     Пример:

# def fnc(text1):
#     def inner(text2):
#         return text1 + text2
#     return inner
#
# fnc2 = fnc("qwer")
# print(fnc2("asdf"))


# add_hello = add_string("Hello")
# print(add_hello("World"))  # "Hello World"
#
#     Напиши функцию-счётчик, которая при каждом вызове увеличивает своё значение на 1 и возвращает результат.
#     Используй замыкание.

# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count +=1
#         return count
#     return inner
#
# fnc = outer()
# print(fnc())
# print(fnc())
# print(fnc())
# print(fnc())
# print(fnc())
# print(fnc())

#     Создай замыкание, которое сохраняет список чисел и имеет внутреннюю функцию для добавления новых чисел в этот список.

# def outer(num):
#     def inner(n):
#         num.append(n)
#         return num
#     return inner
#
# num = [1,2,3,4,5]
# fnc = outer(num)
# print(fnc(6))


#     Напиши функцию, которая возвращает функцию для вычисления квадрата и куба числа.
#     Например:

# def outer():
#     def square(x):
#         return x ** 2
#     def cube(x):
#         return x ** 3
#     return square, cube
#
# square, cube = outer()
# print(square(4))
# print(cube(3))


# square, cube = power_functions()
# print(square(4))  # 16
# print(cube(2))    # 8
#
# Декораторы:
#
#     Создай декоратор, который выводит сообщение перед выполнением функции и после неё.
#     Пример:

# def select(input_fnc):
#     def output_fnc():
#         print("***")
#         input_fnc()
#         print("***")
#     return output_fnc
#
# @select
# def hello():
#     print("Hello!")
#
# hello()


# @decorator
# def say_hello():
#     print("Hello!")
#
#     Напиши декоратор, который измеряет время выполнения функции.
#     Используй time из модуля time.





#     Создай декоратор, который принимает аргумент — текст сообщения, и выводит это сообщение перед выполнением функции.

# def begin(input_fnc):
#     def output_fnc(*args, **kwargs):
#         print("Start")
#         result = input_fnc(*args, **kwargs)
#         return result
#     return output_fnc
#
# @begin
# def start():
#     return 3 + 2
#
# print(start())


#     Напиши декоратор, который проверяет, что аргументы функции являются числами. Если это не так, выводи сообщение об ошибке.

# def proverka(input_fnc):
#     def output_fnc(*args):
#         if all(str(arg).isdigit() for arg in args):
#             return input_fnc(*args)
#         else:
#             print("error")
#     return output_fnc
#
#
# @proverka
# def num(a, b):
#     return a + b
#
# print(num(2, 8))



#     Создай декоратор для функции, который возвращает результат функции в виде строки.
#     Например, если функция возвращает число 10, декоратор должен вернуть "10".
#
# def fnc(input_fnc):
#     def output_fnc(*args, **kwargs):
#         result = input_fnc(*args, **kwargs)
#         string_result = str(result)
#         print(f"Тип результата: {type(string_result)}")
#         return string_result
#     return output_fnc
#
#
# @fnc
# def sum(a, b):
#     return a + b
#
# print(sum(2, 8))


# import time
#
# # Декоратор для измерения времени выполнения
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # Засекаем время до выполнения
#         result = func(*args, **kwargs)  # Выполняем функцию
#         end_time = time.time()  # Засекаем время после выполнения
#         print(f"Время выполнения: {end_time - start_time:.6f} секунд")
#         return result  # Возвращаем результат функции
#     return wrapper
#
# # Декорируемая функция
# @measure_time
# def calculate():
#     return 3 + 2
#
# # Вызов функции
# print(f"Результат: {calculate()}")


# def fnc(fnc2):
#     def fnc1():
#         print("*****")
#         fnc2()
#         print("*****")
#     return fnc1
#
# @fnc
# def fnc3():
#     print (2 + 3)
#
# fnc3()


# def fnc(fnc2):
#     def fnc1(*args):
#         fnc2(*args)
#     return fnc1
#
#
# @fnc
# def fnc3(a, b):
#     print (a + b)
#
# fnc3(2, 3)


def fnc(fnc2):
    def fnc1(*args):
        result = fnc2(*args)
        if result < 0:
            result = 0
        return result
    return fnc1

@fnc
def fnc3(a, b, d):
    return a + b - d

print(fnc3(6, 9, 4))



