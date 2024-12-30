# n = 1
#
# while n <= 5:
#     print(n)
#     n += 1
# print("Работа программы завершена")


# number = 10
#
# while number < 5:
#     print(f"number = {number}")
#     number += 1
# else:
#     print(f"number = {number}. Работа цикла завершена")
# print("Работа программы завершена")

# message = "Hello"
#
# for i in message:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(4,10):
#     print(i, end=" ")

# for i in range(4,10,2):
#     print(i, end="")

# message = "Hello"
# for i in message:
#     print(i)
# else:
#     print(f"Последний символ: {i}. Цикл завершен")


# i = 1
# j = 1
# while i <= 10:
#     while j <= 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1


# for c1 in "ab":
#     for c2 in "ba":
#         print(f"{c1}{c2}")


# number = 0
# while number < 5:
#     number +=1
#     if number == 4:
#         break
#     print(f"number = {number}")


# number = 0
# while number <= 5:
#     number += 1
#     if number == 4:
#         continue
#     print(f"number = {number}")


# n = int(input("Введите число: "))
#
# fct = 1
# сnt = 1
# while  сnt <= n:
#     fct *= сnt
#     сnt += 1
# print(fct)


# n = int(input("Введите число: "))
# s = 0
# while  n != 0:
#     s += n
#     n -= 1
# print(s)


# n = int(input("Введите число: "))
# s = 0
# for i in range(1, (n+1)):
#     if i % 2 != 0:
#         s += 1
# print(f"Нечётных чисел: {s}")
# print(f"Чётных чисел: {n - s}")


# n = int(input("Введите число: "))
# a = []
# while n > 0:
#     a.append(n % 10)
#     n = n // 10
# print(min(a))
# print(max(a))


# n = int(input("Введите число: "))
# max_d = 0
# min_d = 9
# while n > 0:
#     dg = n % 10
#     if dg > max_d:
#         max_d = dg
#     if dg < min_d:
#         min_d = dg
#     n //= 10
# print(max_d)
# print(min_d)





# n = int(input("Введите число: "))
# if n <= 1:
#     print("Число не является простым")
# else:
#     for i in range (2, n // 2 + 1 ):
#         if n % i == 0:
#             print("Число не является простым")
#             break
#     else:
#         print("Число простое")





