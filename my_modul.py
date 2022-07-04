def is_member(my_list: list, item):
    return item in my_list


def item_counter(my_list: list, item):
    return my_list.count(item)


def is_palindrome(my_str: str):
    return my_str == my_str[::-1]


def str_len(my_str: str):
    return len(my_str)


l_case = lambda my_str: my_str.lower()

from math import pi

area_of_the_circle = lambda r: pi * r ** 2

rectangle_area = lambda a, b: a * b

area_of_the_triangle = lambda b, h: b * h / 2

len_dict = lambda my_dict: len(my_dict)

is_member_key = lambda my_dict, key: key in my_dict
