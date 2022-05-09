# Уникальные
def unique(user_list):
    uniq_list = [user_list[0]]
    for item in user_list:
        if item in uniq_list:
            continue
        uniq_list.append(item)
    return uniq_list


mylist = [1, 1, 2, 1, 3, 2, 3]
print(unique(mylist))


# # Сколько четных
# def even_counter(user_list):
#     count = 0
#     for num in user_list:
#         count += int(num % 2 == 0)
#     return count
#
#
# my_list = [1, 10, 2, 4, 6]
# even = even_counter(my_list)
# print(even)
#
#
# # Максимум в списке
# def max_list(user_list):
#     max_num = user_list[0]
#     for num in user_list:
#         if max_num < num:
#             max_num = num
#     return max_num
#
#
# mylist = [1, 3, 2]
# print(max_list(mylist))
#
#
# # На три
# def is_div_three(num):
#     return num % 3 == 0
#
#
# print(is_div_three(4))
# print(is_div_three(3))
#
# # Площадь круга
# import math
#
#
# def ac(r):
#     return math.pi * r ** 2
#
#
# print(ac(4))
# print(ac(1))
