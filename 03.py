# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]

def func(my_list: list):
  new_list = []
  for i in my_list:
    new_list.append(round(i - int(i), 3))
  return new_list

def find_maximum(my_list: list):
  maximum = my_list[0]
  for i in my_list:
    if i > maximum:
      maximum = i
  return maximum

def find_minimum(my_list: list):
  minimum = my_list[0]
  for i in my_list:
    if i < minimum and i != 0:
      minimum = i
  return minimum

new_list = func(my_list)

print(find_maximum(new_list) - find_minimum(new_list))





