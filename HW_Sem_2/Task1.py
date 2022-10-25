# Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
num = input("Введите число: ")
num1 = num
if '.' in num:
    num1 = num.replace('.', '')
elif ',' in num:
    num1 = num.replace(',', '')
sum_nums = 0
for i in num1:
    sum_nums += int(i)
print(f'Введённое число: {num} сумма чисел данного числа: {sum_nums}')
