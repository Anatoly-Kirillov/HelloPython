# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
n = int(input('Введите цифру, обозначающую день недели: '))
if n > 5:
    print('да')
else:
    print('нет')