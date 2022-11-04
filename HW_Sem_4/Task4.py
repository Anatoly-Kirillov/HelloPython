# Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов (значения от 0 до 100) многочлена и записать в файл
#  многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

from Task4_def import generate_expr

power = int(input("Введите степень: "))
res = generate_expr(power, 't4')
with open('task4.txt', 'w', encoding='utf-8') as f:
    f.write(res)
print(res)
