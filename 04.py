# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = 45

def binar(number: int):
  number2 = number
  my_list = []
  while number2 > 1:
    my_list.append(str(number2 % 2))
    number2 //= 2
  my_list.append(str(number2))
  print(my_list)
  my_list.reverse()
  print(my_list)
  number_str = ''.join(my_list)
  print(f'{number} -> {number_str}')

binar(number)


  