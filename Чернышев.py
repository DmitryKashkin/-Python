import pickle
import json
from threading import Thread, Event as Event_th
from multiprocessing import Process, Manager, Event, \
    Value, current_process, cpu_count, Pool, Queue as Queue_proc
import asyncio
from random import randint, random
from time import (time, sleep)
from queue import Queue


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
    sum0 = 0
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


def is_key_from_dict(dict0: dict, key):
    for i in dict0:
        if i == key:
            return True
    return False


def rm_key_from_dict(dict0: dict, key):
    return dict0.pop(key, 'Nicht verstehe')


def min_max_from_dict(dict0: dict):
    dict_val = list(dict0.values())
    return min(dict_val), max(dict_val)


def create_tuple():
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = tuple('67890')
    (a, b, c, d, e) = tuple1
    (f, g, h, i, j) = tuple2
    print(tuple1, tuple2, a, b, c, d, e, f, g, h, i, j)


def val_t_add(tuple1: tuple, val):
    list0 = list(tuple1)
    list0.append(val)
    return tuple(list0)


def convert_to_tuple(list1: list):
    return tuple(list1)


def dict_from_tuple(tuple1: tuple):
    return {i: i for i in tuple1}


def tuple_count(list0: list):
    count_t = 0
    for i in list0:
        # if type(i) == type(tuple()):
        if type(i) is tuple:
            count_t += 1
    return count_t


# print(tuple_count([1,2,3,4,(1,2)]))

def create_set():
    a = set('12345')
    b = {1, 2, 3, 4, 5}
    c = {i for i in b}
    print(a, b, c)


def set_add(set1: set, elem1):
    set1.add(elem1)


def set_discard(set1: set, elem1):
    set1.discard(elem1)


def list_to_set_list(list1: list):
    return list(set(list1))


def merge_set(set1: set, set2: set):
    return set1 | set2


def is_elem_set(set1: set, elem):
    return elem in set1


def write_text_to_file(text1: str):
    my_file = open('text.txt', 'w')
    my_file.write(text1)
    my_file.close()


def read_file():
    my_file = open('text.txt', 'r')
    text1 = my_file.readlines()
    my_file.close()
    return text1


def append_file(text1):
    my_file = open('text.txt', 'a+')
    print(my_file.readlines())
    my_file.write(text1)
    print(text1)
    print(my_file.readlines())


def read_n_of_end(n):
    my_file = open('text.txt', 'r')
    my_text = my_file.readlines()
    print(my_text[-n:])


def len_file():
    my_file = open('text.txt', 'r')
    my_text = my_file.readlines()
    print('в файле ', len(my_text), 'сторк')


def word_in_file(file0: str):
    my_file = open(file0, 'r')
    my_text = my_file.read()

    def cler_my_text(my_text):
        my_text = my_text.replace('.', ' ')
        my_text = my_text.replace('\n', ' ')
        my_text = my_text.replace(',', ' ')
        my_text = my_text.replace('  ', ' ')
        my_text = my_text.split(' ')
        my_text.pop()
        return my_text

    my_text = cler_my_text(my_text)
    my_set = list(set(my_text))
    my_count = [my_text.count(i) for i in my_set]
    my_max = max(my_count)
    for i in range(len(my_count)):
        if my_count[i] == my_max:
            print(my_set[i], my_count[i])


def file_copy(my_file):
    my_copy_file_name = my_file.replace('.txt', '_copy.txt')
    my_file = open(my_file, 'r')
    my_file_copy = open(my_copy_file_name, 'w')
    my_file_copy.write(my_file.read())
    my_file.close()
    my_file_copy.close()


def dict_to_file_to_dict(my_file_name: str, my_dict: dict):
    my_file = open(my_file_name, 'wb')
    pickle.dump(my_dict, my_file)
    my_file.close()
    my_file = open(my_file_name, 'rb')
    my_dict = pickle.load(my_file)
    print(my_dict)


def list_to_file_to_list(my_file_name: str, my_list: list):
    my_file = open(my_file_name, 'wb')
    pickle.dump(my_list, my_file)
    my_file.close()
    my_file = open(my_file_name, 'rb')
    my_list = pickle.load(my_file)
    print(my_list)


def dict_to_file_to_dict_json(my_file_name: str, my_dict: dict):
    json.dump(my_dict, fp=open(my_file_name, 'w'), indent=5)
    my_json = json.load(open(my_file_name))
    print(my_json)


# my_file = 'my_dict.json'
# dict_to_file_to_dict_json(my_file, {1: 1, 2: 2, 3: 3})

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
Напишите программу, выводящую сумму элементов списка [3 01304334 56 613], значения индексов которых делятся 
на без остатка на 3, используя цикл for и while.
13.
Сформируйте список, значения элементов которого находятся в диапазоне от 23 до 35.
92
14.
Сформируйте список, значения элементов которого находятся в диапазоне от 3 до 15 с шагом 4.
15.
Сформируйте список, значения элементов которого находятся в диапазоне от 3 до 25 и без остатка делятся на 3.
16.
Сформируйте словарь из двух списков [3 01 3 0 4 3 3 4 56 6 1 3] и [2, 4,7,26,33], используя встроенную функцию zip. 
Выведите словарь в консоль и объясните, почему он получился такого вида.
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
    print(count1, count2, count3)


def string_to_list(my_string: str):
    my_list = my_string.split(' ')
    print(my_list)
    my_list = [i for i in my_string]
    print(my_list)


def make_matrix(n: int):
    my_matrix = [[i for i in range(n)] for _ in range(n)]
    print(my_matrix)


def print_list_revers(my_list: list):
    print(my_list[::-1])


def print_numbers_1_9_not_5_7():
    print([i for i in range(1, 10) if i != 5 and i != 7])


def my_sum(my_list: list):
    total = 0
    for i in my_list:
        total += i
    print(total)
    total = i = 0
    while i < len(my_list):
        total += my_list[i]
        i += 1
    print(total)
    print(sum(my_list))


def my_sum_div_by_3(my_list: list):
    total = 0
    for i in range(len(my_list)):
        if i % 3 == 0:
            total += my_list[i]
    print(total)
    total = i = 0
    while i < len(my_list):
        if i % 3 == 0:
            total += my_list[i]
        i += 1
    print(total)


def my_list_from_23_to_35():
    print([i for i in range(23, 35)])


def list_3_15_step_4():
    print([i for i in range(3, 15, 4)])


def list_3_25_div_by_3():
    print([i for i in range(3, 25) if i % 3 == 0])


def create_dict(list1: list, list2: list):
    print(dict(zip(list1, list2)))


def season():
    month = input('введите число (месяц)')
    seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
    for months in seasons:
        if int(month) in seasons[months]:
            print(months)
            return


def m_table():
    multiplier = int(input("введите число от 1 до 9"))
    print([multiplier * i for i in range(1, 10)])


def max_3(a, b, c):
    return max(a, b, c)


def sum_list_2(list0: list):
    print(sum(list0))


def multipl(list0: list):
    if list0:
        return list0[0] * multipl(list0[1:])
    else:
        return 1


def invert_str(string: str):
    return string[::-1]


def factorial(n: int):
    if n:
        return n * factorial(n - 1)
    else:
        return 1


def up_low_case(my_str: str, up_count=0, low_count=0):
    if not my_str:
        return up_count, low_count
    if my_str[0].islower():
        low_count += 1
        return up_low_case(my_str[1:], up_count, low_count)
    if my_str[0].isupper():
        up_count += 1
        return up_low_case(my_str[1:], up_count, low_count)
    return up_low_case(my_str[1:], up_count, low_count)


def rm_duble(my_list: list):
    return set(my_list)


def print_even(my_list: list):
    print([my_list[_] for _ in range(len(my_list)) if _ % 2 == 0])


def is_palindrome(my_str: str):
    print(my_str == my_str[::-1])


def tag_b(my_func):
    def wrap(*args, **kwargs):
        return '<b>' + my_func(*args, **kwargs) + '</b'

    return wrap


@tag_b
def print_str(my_str: str):
    return my_str


def square_decorator(my_func):
    def wrap(*args, **kwargs):
        return my_func(*args, **kwargs) ** 2

    return wrap


max_3 = square_decorator(max_3)


def upper_decorator(my_func):
    def wrap(*args, **kwargs):
        return my_func(*args, **kwargs).upper()

    return wrap


invert_str = upper_decorator(invert_str)


def my_decorator(my_func):
    def wrap(*args, **kwargs):
        print(*args, **kwargs)

    return wrap


@my_decorator
def my_func(a, b, c):
    return a * b ** c


def generator_23_37():
    for _ in range(23, 37):
        yield _


def generator_5_37_step_4():
    for _ in range(5, 37, 4):
        yield _


i = (_ for _ in range(0, 15))

my_list = [3, 0, 1, 3, 0, 4, 3, 3, 4, 56, 6, 13]
my_iter = (_ ** 2 for _ in my_list)


def custom_generator(step=1):
    for _ in range(0, 100, step):
        yield _


class TestClass:
    def my_func(self):
        c = 3
        c += 1
        return c

    a = 2


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class BaseTextTest:
    name2 = 12

    def __init__(self):
        self.name = 11


class Sqare:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        self.__s = a * b

    def __lt__(self, other):
        return self.__s < other.__s

    def __eq__(self, other):
        return self.__s == other.__s

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a
        self.__s = a * self.__b
        print(self.__a, self.__b, self.__s)

    @property
    def area(self):
        return self.__s


class Json:

    def __init__(self, file_name):
        self.file_name = file_name
        self.dict = json.load(open(self.file_name))

    def read(self):
        return self.dict['base']

    def write(self):
        json.dump(self.dict, fp=open(self.file_name, 'w'), indent=5)

    def __str__(self):
        return str(json.load(open(self.file_name))['base'][1])

    def add(self, pos, key, val):
        self.dict['base'][pos - 1][key] = val

    def delete(self, pos, key):
        del (self.dict['base'][pos - 1][key])

    def modify(self, pos, key, val):
        self.dict['base'][pos - 1][key] = val


class SquareMax:
    def __init__(self, squares: list):
        self.__max = max(squares, key=lambda _: _.area)

    def __str__(self):
        return str(self.__max.area)


class Numbers:
    def __init__(self, number):
        if isinstance(number, int):
            self.dec = number
            self.binary = bin(number)
        else:
            self.binary = number
            self.dec = int(number, base=2)


class Nod:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    def nod(self):
        self.__nod = 1
        for i in range(2, min(self.__a, self.__b)):
            if (not (self.__a % i)) and (not (self.__b % i)):
                self.__nod = i
                break
        return self.__nod


class QuadraticEquation:
    def __init__(self, a=1, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.__D = self.b ** 2 - 4 * a * c
        if self.__D >= 0:
            self.x1 = (-b + self.__D ** 0.5) / (2 * a)
            self.x2 = (-b - self.__D ** 0.5) / (2 * a)
        elif self.__D < 0:
            self.x1 = self.x2 = None


class Member:
    def __init__(self, first_name, last_name):
        self.propertys = {'first_name': first_name, 'last_name': last_name}


class Notebook:
    def __init__(self, file_name):
        self.note = []
        self.file_name = file_name

    def __getattr__(self, item):
        print(str(item) + ' is not defained')
        return str(item) + ' is not defained'

    def __str__(self):
        return str(self.note)

    def add_note(self, fio, tel, e_mail, dr):
        self.note.append({'fio': fio, 'tel': tel, 'e_mail': e_mail, 'dr': dr})

    def load(self):
        self.note = json.load(open(self.file_name))

    def save(self):
        json.dump(self.note, fp=open(self.file_name, 'w'), indent=5)


def intro_function(text, index): print(text[index])


class MyMath:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        self.result = self.a * self.b
        return self.result

    def div(self):
        return self.a / self.b


class MyExeption(Exception):
    ...


class MyMathExceptIfArg0(MyMath):
    def __init__(self, a, b):
        super().__init__(a, b)

    def __getattribute__(self, item):
        if object.__getattribute__(self, 'a') == 0 or object.__getattribute__(self, 'b') == 0:
            raise MyExeption('Argument a or b is 0')
        return object.__getattribute__(self, item)


class MyMathZeroToOne(MyMath):
    """Напишите класс, реализующий такие арифметические действия, как деление и умножение.
    Если одно из значений при вызове операции равно нулю, генерируется исключение,
    значение ноль меняется на 1 и вычисление операции продолжается."""

    def __init__(self, a, b):
        super().__init__(a, b)

    def if_zero_decorator(func):
        def wrapper(self):
            try:
                if self.a != 0 and self.b != 0:
                    return func(self)
                if self.a == 0:
                    self.a = 1
                if self.b == 0:
                    self.b = 1
                raise MyExeption('Argument a or b is 0')
            except MyExeption as my_ex:
                print(my_ex)
                return func(self)

        return wrapper

    @property
    @if_zero_decorator
    def mul(self):
        return self.a * self.b

    @property
    @if_zero_decorator
    def div(self):
        return self.a / self.b


def if_zero_decorator(class_method):
    def wrapper(self):
        try:
            if self.a != 0 and self.b != 0:
                return class_method(self)
            if self.a == 0:
                self.a = 1
            if self.b == 0:
                self.b = 1
            raise MyExeption('Argument a or b is 0')
        except MyExeption as my_ex:
            print(my_ex)
            return class_method(self)

    return wrapper


class MyMathZeroToOne2(MyMath):
    """Напишите класс, реализующий такие арифметические действия, как деление и умножение.
    Если одно из значений при вызове операции равно нулю, генерируется исключение,
    значение ноль меняется на 1 и вычисление операции продолжается."""

    def __init__(self, a, b):
        super().__init__(a, b)

    @property
    @if_zero_decorator
    def mul(self):
        super().mul()
        return self.result

    @property
    @if_zero_decorator
    def div(self):
        return self.a / self.b


def up_case(_: str) -> str:
    try:
        if _ == '':
            raise Exception('str is none')
    except Exception as my_ex:
        print(my_ex)
        return ''
    return _.upper()


def is_member(my_list: list, item) -> bool:
    if len(my_list) == 0:
        raise Exception('list is empty')
    return item in my_list


class Exception_If_P(Exception):
    ...


def test_p_exception(my_string: str):
    if 'p' in my_string:
        raise Exception_If_P


def file_read(file_name: str, box: list, event: Event):
    print('read start')
    mode = 'rb'
    with open(file_name, mode) as file_source:
        box[0] = file_source.read()
        print('read stop')
    # print(box[0])
    event.set()


def file_write(file_name: str, box: list, event: Event) -> None:
    event.wait()
    print('write start')
    mode_write = 'wb'
    # print(box[0])
    with open(file_name, mode_write) as file_destination:
        file_destination.write(box[0])
    print('write stop')


def test_threads():
    box = ['']
    file_name, mode = 'prazdnik.xml', 'rb'
    file_name_copy, mode_write = 'prazdnik_copy.xml', 'wb'
    thread_one = Thread(target=file_read, args=(file_name, box))
    thread_two = Thread(target=file_write, args=(file_name_copy, box))
    thread_one.start()
    thread_one.join()
    thread_two.start()
    thread_two.join()
    print('end')


def test_processes():
    event = Event()
    box = Manager().list()
    box.append('')
    file_name, mode = 'prazdnik.xml', 'rb'
    file_name_copy, mode_write = 'prazdnik_copy.xml', 'wb'
    process_read = Process(target=file_read, args=(file_name, box, event))
    process_write = Process(target=file_write, args=(file_name_copy, box, event))
    process_read.start()
    process_write.start()
    process_read.join()
    process_write.join()


async def file_read_async(file_name: str, box: list):
    print('read start')
    mode = 'rb'
    # with open(file_name, mode) as file_source:
    #     box[0] = file_source.read()
    await asyncio.sleep(1.0)
    print('read stop')


async def file_write_async(file_name: str, box: list) -> None:
    print('write start')
    mode_write = 'wb'
    # with open(file_name, mode_write) as file_destination:
    #     file_destination.write(box[0])
    print('write stop')


def test_async():
    box = ['']
    file_name, mode = 'prazdnik.xml', 'rb'
    file_name_copy, mode_write = 'prazdnik_copy.xml', 'wb'
    loop = asyncio.get_event_loop()
    functions = asyncio.wait([file_read_async(file_name, box), file_write_async(file_name_copy, box)])
    loop.run_until_complete(functions)


async def test_async_2():
    box = ['']
    file_name, mode = 'prazdnik.xml', 'rb'
    file_name_copy, mode_write = 'prazdnik_copy.xml', 'wb'
    functions = asyncio.gather(file_read_async(file_name, box), file_write_async(file_name_copy, box))
    await functions


async def test_async_3():
    box = ['']
    file_name, mode = 'prazdnik.xml', 'rb'
    file_name_copy, mode_write = 'prazdnik_copy.xml', 'wb'
    task_one = asyncio.create_task(file_read_async(file_name, box))
    task_two = asyncio.create_task(file_write_async(file_name_copy, box))
    await task_one
    await task_two


def print_matrix(matrix: list) -> None:
    for i in matrix:
        print(i)


def matrix_generator(i: int, j: int, k: int) -> tuple:
    return [[randint(100, 999) for _ in range(j)] for __ in range(i)] \
        , [[randint(100, 999) for _ in range(k)] for __ in range(j)]


def result_line(matrix_one, matrix_two, matrix_new, line_number):
    def result(list_one: list, list_two: list) -> int:
        res = 0
        for a, b in zip(list_one, list_two):
            # print(a,b)
            res += a * b
        return res

    for i in range(len(matrix_two[0])):
        matrix_new[line_number][i] = result(matrix_one[line_number], [_[i] for _ in matrix_two])


def result_line_pool_process(matrix_one, matrix_two, matrix_new, line_number):
    def result(list_one: list, list_two: list) -> int:
        res = 0
        for a, b in zip(list_one, list_two):
            # print(a,b)
            res += a * b
        return res

    res = []

    for i in range(len(matrix_two[0])):
        res.append(result(matrix_one[line_number], [_[i] for _ in matrix_two]))
    return res


def result_line_pool_starmap(matrix_one_line, matrix_two):
    # print(matrix_one_line)
    # print(matrix_two)
    def result(list_one: list, list_two: list) -> int:
        res = 0
        for a, b in zip(list_one, list_two):
            # print(a,b)
            res += a * b
        return res

    res = []

    for i in range(len(matrix_two[0])):
        res.append(result(matrix_one_line, [_[i] for _ in matrix_two]))
    return res


def speed_test_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time()
        res = func(*args, **kwargs)
        time_end = time()
        # for i in args:
        #     if type(i) == list:
        #         print_matrix(i)
        # print_matrix(args[2])
        print('time ', time_end - time_start)
        return res

    return wrapper


@speed_test_decorator
def mul_matrix(matrix_one, matrix_two, matrix_new, i):
    for ii in range(i):
        result_line(matrix_one, matrix_two, matrix_new, ii)


def result_line_multiprocess(matrix_one, matrix_two, matrix_new, line_number):
    def result(list_one: list, list_two: list) -> int:
        res = 0
        for a, b in zip(list_one, list_two):
            res += a * b
            # print(res)
        return res

    res = []
    for i in range(len(matrix_two[0])):
        res.append(result(matrix_one[line_number], [_[i] for _ in matrix_two]))
    matrix_new[line_number] = res


@speed_test_decorator
def mul_matrix_multiprocess(matrix_one, matrix_two, matrix_new, i):
    process = list(range(i))
    for ii in range(i):
        process[ii] = Process(target=result_line_multiprocess, args=(matrix_one, matrix_two, matrix_new, ii))
        process[ii].start()
    for ii in range(i):
        process[ii].join()


@speed_test_decorator
def mul_matrix_multithread(matrix_one, matrix_two, matrix_new, i):
    threads = list(range(i))
    for ii in range(i):
        threads[ii] = Thread(target=result_line, args=(matrix_one, matrix_two, matrix_new, ii))
        threads[ii].start()
    for ii in range(i):
        threads[ii].join()


def main_mul_matrix_multiprocess():
    matrix_one, matrix_two = matrix_generator(6, 1000, 5000)
    i = len(matrix_one)
    j = len(matrix_two)
    k = len(matrix_two[0])
    matrix_new = Manager().list([[_ for _ in range(k)] for __ in range(i)])
    mul_matrix_multiprocess(matrix_one, matrix_two, matrix_new, i)


def main_mul_matrix_multithread():
    matrix_one, matrix_two = matrix_generator(6, 1000, 5000)
    i = len(matrix_one)
    j = len(matrix_two)
    k = len(matrix_two[0])
    matrix_new = list([[_ for _ in range(k)] for __ in range(i)])
    mul_matrix_multithread(matrix_one, matrix_two, matrix_new, i)


def mul_matrix_pool_process(matrix_one, matrix_two, matrix_new, i):
    res = [result_line_pool_process(matrix_one, matrix_two, matrix_new, ii) for ii in range(i)]
    # sleep(5)
    # print(res)
    return res


def main_mul_matrix():
    matrix_one, matrix_two = matrix_generator(6, 1000, 5000)
    i = len(matrix_one)
    j = len(matrix_two)
    k = len(matrix_two[0])
    matrix_new = [[0 for _ in range(k)] for __ in range(i)]
    mul_matrix(matrix_one, matrix_two, matrix_new, i)


def main_mul_matrix_pool_process():
    matrix_one, matrix_two = matrix_generator(6, 1000, 5000)
    i = len(matrix_one)
    j = len(matrix_two)
    k = len(matrix_two[0])
    matrix_new = [[0 for _ in range(k)] for __ in range(i)]
    pool_size = cpu_count() * 2
    with Pool(processes=pool_size) as pool:
        pool_res = [pool.apply_async(mul_matrix_pool_process, (matrix_one, matrix_two, matrix_new, i,)) for _ in
                    range(pool_size)]
        new_line = [res.get() for res in pool_res]
        print(new_line)


@speed_test_decorator
def main_mul_matrix_pool_starmap():
    matrix_one, matrix_two = matrix_generator(6, 1000, 5000)
    i = len(matrix_one)
    j = len(matrix_two)
    k = len(matrix_two[0])
    pool_size = cpu_count() * 2
    with Pool(processes=pool_size) as pool:
        pool_res = pool.starmap(result_line_pool_starmap, zip(matrix_one, [matrix_two for _ in matrix_one]))
        # new_line = [res.get() for res in pool_res]
        # print(pool_res)


def count_add(my_count, step):
    my_count.value += step


def count_in_multiprocess():
    my_count = Value('i', 0)
    step = 5
    number_of_processes = 100
    process = list(range(number_of_processes))

    for i in range(number_of_processes):
        process[i] = Process(target=count_add, args=(my_count, step))
        process[i].start()
    for i in range(number_of_processes):
        process[i].join()
    sleep(1)
    print(my_count.value)


# @speed_test_decorator
def median(list_one: list) -> int:
    list_one.sort()
    res = list_one[len(list_one) // 2]
    print(res)
    return res


def list_generator(len_list: int) -> list:
    list_of_lists = [[random() for _ in range(len_list)] for __ in range(10)]
    return list_of_lists


def median_main():
    list_of_lists = list_generator(500001)
    for list_ in list_of_lists:
        median(list_)


def median_multipocess_main():
    list_of_lists = list_generator(500001)

    @speed_test_decorator
    def median_pool():
        pool_size = cpu_count() * 2
        with Pool(processes=pool_size) as pool:
            pool_res = pool.map(median, list_of_lists)
            # print(pool_res)

    median_pool()


def median_multithreads_main():
    list_of_lists = list_generator(500001)

    @speed_test_decorator
    def median_threads(list_of_lists: list):
        threads = []

        for i in range(len(list_of_lists)):
            threads.append(Thread(target=median, args=(list_of_lists[i],)))
            threads[i].start()

    median_threads(list_of_lists)


def queue_print(my_queue, i, event):
    # print(my_queue, i, event)
    while not my_queue.empty():
        event.wait(1)
        print(my_queue.get(), ' thread (process) ', i)
        event.set()
        sleep(0.1)


def queue_put(my_queue: Queue):
    for i in range(20):
        my_queue.put(random())


def test_queue():
    def queue_threads():
        threads = []
        for i in range(4):
            threads.append(Thread(target=queue_print, args=(my_queue, i, event)))
            threads[i].start()
        for i in range(4):
            threads[i].join()

    def queue_process():
        proces = []
        for i in range(4):
            proces.append(Process(target=queue_print, args=(my_queue, i, event)))
            proces[i].start()
        for i in range(4):
            proces[i].join()

    event = Event_th()
    my_queue = Queue()
    queue_put(my_queue)
    print('threads')
    queue_threads()

    event = Event()
    my_queue = Queue_proc()
    queue_put(my_queue)
    print('process')
    queue_process()


def count_plus_5(my_count, event: Event(), proc_id):
    while my_count.value < 50:
        print('process ', proc_id, ' start')
        if my_count.value != 0:
            event.wait()
        for i in range(5):
            my_count.value += 1
        event.set()
        print('process ', proc_id, ' sleep')
        sleep(0.01)



def count_5_plus_main():
    my_count = Value('i', 0)
    event = Event()
    my_process = [Process(target=count_plus_5, args=(my_count, event, 1)),
                  Process(target=count_plus_5, args=(my_count, event, 2))]
    my_process[0].start()
    my_process[1].start()
    my_process[0].join()
    my_process[1].join()
    print(my_count.value)


if __name__ == '__main__':
    count_5_plus_main()
