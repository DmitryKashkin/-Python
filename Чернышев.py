def len_str(string0=''):
    print(len(string0))
    j = 0
    for i in string0:
        j += 1
    print(j)


def new_str(str0=''):
    if len(str0) < 2:
        return ''
    return str0[0:2] + str0[-2:]


def replace_str(str0='', sym=''):
    return str0.replace(sym, '$')


def revers_str(str0=''):
    # str0 = list(str0)
    # str0.reverse()
    # return ''.join(str0)
    return str0[::-1]


def count(str0=''):
    key = set(str0)
    val = [str0.count(c) for c in key]
    return dict(zip(key, val))


def split_str(str0=''):
    # str1 = ''.join([])
    return str0[::2], str0[1::2]


def del_str(str0='', str1=''):
    return str0.replace(str1, '')


def upper_lower(str0=''):
    return str0.upper(), str0.lower()


def index_str(str0=''):
    return dict(zip(str0, range(len(str0))))


def is_str(str0='', str1=''):
    return str1 in str0


def symbol_in_str(str0=''):
    keys = set(str0)
    val = [str0.count(c) for c in keys]
    symbols = dict(zip(keys, val))
    max_val = max(val)
    for i in symbols:
        if symbols[i] == max_val:
            return i


def swapcase_str(str0: str) -> str:
    return str0.swapcase()


def sum_list(list0: list) -> int:
    sum0 = sum1 = 0
    for i in list0:
        sum0 += i
    return sum0


def multiply(list0: list, x: int) -> list:
    list0 = [i * x for i in list0]
    return list0


def min_max(list0: list) -> tuple:
    return min(list0), max(list0)


def rm_duplicates(list0: list) -> list:
    for i in list0:
        if list0.count(i) > 1:
            list0.remove(i)
    return list0


def list_copy(list0: list) -> tuple:
    list1 = list0.copy()
    list2 = [i for i in list0]
    list3 = list0[::]
    return list1, list2, list3


def merge_list(list0: list, list1: list):
    list3 = list0 + list1
    print(list3)
    list0.extend(list1)
    print(list0)


def swap_item(list0: list, n: int):
    if n + 1 > len(list0) - 1:
        print('error')
        return
    list0[n], list0[n + 1] = list0[n + 1], list0[n]
    print(list0)


def list_to_numbr(list0: list):
    return int(''.join([str(i) for i in list0]))


def dict_init():
    dict1 = {0: 10, 1: 20}
    dict1[2], dict1[3] = 30, 40
    print(dict1)
    dict1 = dict(key1='val', key2='val')
    print(dict1)


def merge_dict(dict1: dict, dict2: dict):
    dict3 = {}
    dict3.update(dict1)
    dict3.update(dict2)
    return dict3


def is_key_from_dict(dict0: {}, key):
    for i in dict0:
        if i == key:
            return True
    return False


dict1 = {1: 1, 2: 2}
dict2 = {3: 3, 4: 4}
print(is_key_from_dict(dict1, 3))


"""
1. Выведите все символы из строки
«Данная часть была посвящена больше синтаксису Python и вопросам документации кода»,
значения индексов которых делятся на 2.

2. Выведите все символы из строки
«Данная часть была посвящена больше синтаксису Python и вопросам документации кода»,
значения индексов которых без остатка делятся на 3, но не делятся на 4.

3. Выведите все символы из строки
(Данная часть была посвящена больше синтаксису Python и вопросам документации кода»,
значения индексов которых при делении на 6 дают остаток 2, 4, и 5.

4. Выведите числа из диапазона от 1 до 10, используя цикл for и while.

5. Выведите числа из диапазона от -20 до 20 с шагом 3, используя цикл for и while.

6. Посчитайте количество вхождений элемента со значением «3» в следующем списке:
[3,0,1,3,0,4,3,3,4,56,6,1,3], используя цикл for, while и метод count.

7. Сформируйте список из элементов строки «список доступных атрибутов»,
используя механизм списковых включений и цикл for.
8.
Сформируйте единичную матрицу N х N, используя механизм списковых включений.
9.
Напишите программу, выводящую элементы списка [3 01304334 56 6 1 3] в обратной последовательности.
10.
Напишите программу, которая выводит числе в диапазоне от 1 до 9, кроме 5 и 7.
11.
Напишите программу, выводящую сумму элементов списка [3 01 304334 56 61 3], используя цикл for, while и метод sum.
12.
Напишите программу, выводящую сумму элементов списка [3 01304334 56 613], значения индексов которых делятся на без остатка на 3, используя цикл for и while.
13.
Сформируйте список, значения элементов которого находятся в диапазоне от 23 до 35.
92
14.
Сформируйте список, значения элементов которого находятся в диапазоне от 3 до 15 с шагом 4.
15.
Сформируйте список, значения элементов которого находятся в диапазоне от 3 до 25 и без остатка делятся на 3.
16.
Сформируйте словарь из двух списков [3 01 3 0 4 3 3 4 56 6 1 3] и [2, 4,7,26,33], используя встроенную функцию zip. Выведите словарь в консоль и объясните, почему он получился такого вида.
17.
Выведите различными способами в консоль элементы списка [3 01304334 56 6 1 3] с их индексами.
18.
Напишите программу, которая считывает целое число (месяц), после чего выводит сезон к которому этот месяц относится.
19.
Напишите программу, выводящую среднее из трех значений.
20.
Напишите программу, выводящую таблицу умножения для задаваемого пользователем числа от 1 до 9 (включительно).
"""


def even_symbol(string1):  # 1
    return [s for index, s in enumerate(string1) if index % 2 == 0]


def even_symbol_3_4(string1):  # 2
    return [s for index, s in enumerate(string1) if index % 3 == 0 and index % 4 != 0]


def even_symbol_6_2_4_5(string1):  # 3
    return [(s, index) for index, s in enumerate(string1) if (index % 6) in [2, 4, 5]]


def nums_1_10():  # 5
    for i in range(-20, 21, 3):
        print(i, end=' ')
    print('')
    i = -20
    while i <= 20:
        print(i, end=' ')
        i += 3


def count_3():  # 6
    count1 = 0
    for i in [3, 0, 1, 3, 0, 4, 3, 3, 4, 56, 6, 1, 3]:
        if i == 3:
            count1 += 1
    list0 = [3, 0, 1, 3, 0, 4, 3, 3, 4, 56, 6, 1, 3]
    count2 = i = 0
    while i < len(list0):
        if list0[i] == 3:
            count2 += 1
        i += 1
    count3 = list0.count(3)
    return count1, count2, count3

# string1 = 'Данная часть была посвящена больше синтаксису Python и вопросам документации кода'
# print(count_3())
