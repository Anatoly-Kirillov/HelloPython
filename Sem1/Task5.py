# Напишите программу, которая принимает на вход число и проверяет
# кратно ли оно 5 и 10 или 15, но не 30.
n = int(input('Введите число: '))
if ((n % 5 == 0 and n % 10 == 0) or n % 15 == 0) and n % 30 != 0:
    print(f"Число {n} кратно 5 и 10 или 15, но не кратно 30")
else:
    print(f"Число {n} не подходит под условие")