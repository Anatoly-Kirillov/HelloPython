# Реализуйте алгоритм перемешивания списка.
import numbers
from random import randint
a = int(input('Введите число обозначающее количество чисел в списке:'))
num_list = [i for i in range(a)]
print(f"Первоначальный список: {num_list}")
for i in range(len(num_list)):
    rand = randint(0, a)
    num_list[i], num_list[rand] = num_list[rand], num_list[i]
print(f"Перемешанный список: {num_list}")