# Английский словарь
en_dict = {}
n = int(input())
for i in range(n):
    word_key = input().split(' - ')
    en_dict[word_key[0]] = word_key[1].split(', ')
print(en_dict)


# # средний возраст всех друзей и самое длинное имя
# n = int(input())
# friends = []
# spec = {}
# for i in range(n):
#     name = input()
#     age = int(input())
#     friends.append({'name': name, 'age': age})
# long_name = friends[0]['name']
# all_age = 0
# for item in friends:
#     all_age += item['age']
#     if len(long_name) < len(item['name']):
#         long_name = item['name']
# print(all_age / n)
# print(long_name)


# # Старший и младший
# n = int(input())
# friends = []
# spec = {}
# for i in range(n):
#     name = input()
#     age = int(input())
#     friends.append({'name': name, 'age': age})
# jun = friends[0]
# for item in friends:
#     if jun['age'] > item['age']:
#         jun = item
# print(jun['name'])
#

# # Фрукты
# k = int(input())
# fruits = {}
# for i in range(k):
#     fruit = input()
#     q = int(input())
#     fruits[fruit] = q
# print(fruits)
