# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.

a = int(input('Введите число N: '))
# from random import randint
# for i in range(a):
#     print(randint(-100, 100), end=' ')
num_list = [1]
for i in range(a-1):
    num_list.append(num_list[i]*(-3))
print(*num_list, sep=', ')
