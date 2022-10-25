# Задайте список из N элементов,
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

num = int(input("Введите число: "))
num_list = [i for i in range(-num, num + 1)]
indexes = open('Task4.txt', 'r')
prod_num = 1
for i in indexes:
    if int(i) < len(num_list):
        prod_num *= num_list[int(i)]
print(num_list, prod_num, sep='\n')
indexes.close()