# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal

num = Decimal(input("Введите вещественное число: "))
num_d = Decimal(input("Введите вещественное число обозначающее точность.\n"
                      "От 10^-1 до 10^-1: "))
num_r = num.quantize(Decimal(f'{1 + num_d}'))
print(f'Введённое число: {num}\n'
      f'Точность: {num_d}\n'
      f'Результат: {num_r}')