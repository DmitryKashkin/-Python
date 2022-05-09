# Создайте список из случайных чисел.
# Найдите количество различных элементов в нем
# from random import randint
# nums = []
# # заполняем список
# for i in range(10):
#     nums.append(randint(1, 10))
# print(nums)
# var = 0
# for num in nums:
#     if nums.count(num) == 1:
#         var += 1
# print(var)

# Создайте список из случайных чисел.
# Найдите второй максимум.
# from random import randint
# nums = []
# # заполняем список
# for i in range(10):
#     nums.append(randint(1, 10))
# print(nums)
# max1 = nums[0]
# max2 = max1
# for num in nums:
#     if num > max1:
#         max2 = max1
#         max1 = num
#     elif num != max1 and num > max2:
#         max2 = num
# print(max1, max2)


# Создайте список из случайных чисел.
# Найдите максимальное количество его одинаковых элементов
# from random import randint
# nums = []
# # заполняем список
# for i in range(10):
#     nums.append(randint(1, 10))
# print(nums)
# max = 1
# for num in nums:
#     if max < nums.count(num):
#         max = nums.count(num)
# print(max)



# Создайте список из случайных чисел.
# Найдите номер его последнего локального максимума
# (локальный максимум — это элемент,
# который больше любого из своих соседей).
# from random import randint
# nums = []
# # заполняем список
# for i in range(10):
#     nums.append(randint(1, 10))
# print(nums)
#
# max_in_nums = 0
# for i in range(len(nums) - 2):
#     if nums[i+1] > nums[i] and nums[i+1] > nums[i+2]:
#         max_in_nums = i+1
# print(max_in_nums)

# Создайте список из случайных чисел
# и найдите наибольший элемент в нем.
# Найдите наименьший элемент
# Найдите сумму элементов
# Найдите среднее арифметическое
# from random import randint
# int_nums = []
# for i in range(10):
#     int_nums.append(randint(1, 10))
# print(int_nums)
# max = int_nums[0]
# min = int_nums[0]
# summa = 0
# for num in int_nums:
#     if num > max:
#         max = num
#     if num < min:
#         min = num
#     summa += num
# print(max, min, summa)
# print(summa / len(int_nums))

# Даны два списка, удалите все элементы
# первого списка из второго
# a = [1, 3, 4, 5]
# b = [4, 5, 6, 7]
# i = 0
# while i < len(b):
#     if b[i] in a:
#         b.pop(i)
#     else:
#         i += 1
# print(b)

# Создайте список из введенной пользователем строки
# и удалите из него символы 'a', 'e', 'o'
# l = list(input())
# del_list = ['a', 'o', 'e']
# i = 0
# while i < len(l):
#     if l[i] in del_list:
#         l.pop(i)
#     else:
#         i += 1
# print(l)

# Создайте пустой список
# и добавьте в него 10 случайных чисел и выведите их
# Удалите все элементы из списка, созданного в задании
# from random import randint
# int_nums = []
# for i in range(10):
#     int_nums.append(randint(1, 10))
# print(int_nums)
# int_nums.clear()
# print(int_nums)


# Создайте список из 5 элементов.
# Сделайте срез от второго индекса до четвертого
# numbers = [2, 4, 6, 8, 10]
# part_of_num = numbers[2:4]
# print(part_of_num)

# Создайте список из 10 четных чисел
# и выведите его с помощью цикла for
# numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# for num in numbers:
#     print(num)

# Фибоначчи
# n = int(input())
# fib0 = 1
# fib = 0
# for i in range(n):
#     fib += fib0
#     fib0 = fib - fib0
# print(fib)

# Факториал
# n = int(input())
# fact = 1
# for x in range(n):
#     fact *= (x+1)
# print(fact)

# Максимум
# maxNum = int(input())
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     if maxNum < num:
#         maxNum = num
# print(maxNum)

# Сумма чисел
# summa = 0
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     summa += num
# print(summa)


# От A до B на три
# a = int(input())
# b = int(input())
# while a <= b:
#     if a % 3 == 0:
#         print(a)
#     a += 1

# Четные от A до B
# a = int(input())
# b = int(input())
# while a > b:
#     if a % 2 == 0:
#         print(a)
#     a -= 1

# Сумма дробей (часть вторая)
# n = int(input())
# sum = 0
# for x in range(n):
#     sum += 1 / (x + 1)
# print(sum)

# Сумма дробей (часть первая)
# n = int(input()) + 1
# sum = 0
# for x in range(n):
#     sum += 1 + x / 10
# print(sum)


# Сумма четных от K до N
# k = int(input())
# n = int(input()) + 1
# if k % 2 !=0:
#     k += 1
# sum = 0
# for x in range(k, n, 2):
#     sum += x
# print(sum)


# Сумма от K до N
# k = int(input())
# n = int(input()) + 1
# sum = 0
# for x in range(k, n):
#     sum += x
# print(sum)


# Вывод чисел от K до N
# k = int(input())
# n = int(input()) + 1
# for x in range(k, n):
#     print(x)

# Вывод чисел от 0 до N
# num = int(input()) + 1
# for x in range(num):
#     print(x)

# Конь (финальный босс)
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (x1 < 1 or x1 > 8 or x2 < 1 or x2 > 8 or
#         y1 < 1 or y1 > 8 or y2 < 1 or y2 >8):
#     print('Error')
# elif ((((x1 - x2) ** 2 == 4 and (y1 - y2) ** 2 == 1) or
#       ((x1 - x2) ** 2 == 1 and (y1 - y2) ** 2 == 4))):
#     print('yes')
# else:
#     print('no')

# Описание числа
# num = int(input())
# if num == 0:
#     print('null')
# elif num > 0:
#     print('polozhitelnoe', end=' ')
# else:
#     print('otritsatelnoe', end=' ')
# if  (num % 2) == 0 and num != 0:
#     print('chetnoe chislo')
# elif num != 0:
#     print('nechetnoe chislo')


# День недели
# day = int(input())
# if  day == 6 or day == 7:
#     print('Vihodnoy')
# elif day >= 1 and day <= 5:
#     print('budni')

# Время суток
# hr = int(input())
# if hr >= 5 and hr <= 11:
#     print('Utro')
# elif hr >= 12 and hr <= 17:
#     print('Den')
# elif hr >= 18 and hr <= 22:
#     print('Vecher')
# elif hr == 23 or (hr >= 0 and hr <= 4):
#     print('noch')
# else:
#     print('Error')

# Треугольник?
# sideA = int(input())
# sideB = int(input())
# sideC = int(input())
# if (sideA + sideB > sideC and
#         sideC + sideB > sideA and
#         sideC + sideA > sideB):
#     print('yes')
# else:
#     print('no')

# Четырехзначное?
# number1 = int(input())
#
# if number1 // 1000 > 0:
#     print('yes')
# else:
#     print('no')

# Меньшее из двух
# number1 = int(input())
# number2 = int(input())
# if number1 > number2:
#     print(number2)
# else:
#     print(number1)


# Часы (финальный босс)
# number = int(input())
# print(number // 3600,  (number // 60) % 60,  number % 60)

# Разные цифры
# number = int(input())
# print(number // 100 != number % 100 // 10 and
#       number // 100 != number % 10 and
#       number % 100 // 10 != number % 10)

# Цифры трехзначного
# number = int(input())
# print(number // 100 + number % 100 // 10 + number % 10)

# Цифры двузначного
# number = int(input())
# print(number // 10 + number % 10)

# Последняя цифра
# number = int(input())
# print(number % 10)