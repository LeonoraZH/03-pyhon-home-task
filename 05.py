# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input("Введите число: "))
array = []
array2 = []


def fill_fibonachi(array: list, n: int):
  for i in range(0, n + 1):
    if i == 0:
      array.insert(i, 0)
    elif i == 1:
      array.insert(i, 1)
    else:
      element = array[i - 1] + array[i - 2]
      array.insert(i, element)
  return array


def fill_negafibonachi(array: list, n: int):
  for i in range(0, n):
    if i == 0:
      array.insert(i, 1)
    elif i == 1:
      array.insert(i, -1)
    else:
      element = (abs(array[i - 1]) + abs(array[i - 2])) * (-1) ** i
      array.insert(i, element)
  return array


fill_negafibonachi(array2, n)
array2.reverse()
array2 += array
print(array2)



