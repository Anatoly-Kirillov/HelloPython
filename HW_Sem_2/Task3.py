# Задайте список из n чисел последовательности (1 + 1 / n) ** n
#  и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037
num = int(input("Введите число: "))
sum_list = [(1 + 1 / n) ** n for n in range(1, num + 1)]
print(f'{num} -> {sum(sum_list)}')