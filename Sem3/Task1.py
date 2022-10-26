# Задайте список.Напишите программу, которая определит,
#  присутствует ли в заданном списке строк некое число.
n = input('Введите число, которое будем искать: ')
list = ['lkhbf456, kg867fm, lkljkh987n']
for i in list:
    # i = str(i)
    if n in i:
        print('Yes')
        break
else:
    print('No')

