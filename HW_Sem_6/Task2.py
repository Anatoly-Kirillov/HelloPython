# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
#  список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]
from random import randint

lst = [randint(1, 10) for _ in range(10)]

result = {i: 0 for i in set(lst)}
for i in lst:
    result[i] += 1
print(f'{lst} => {list(filter(lambda x: result[x] == 1, result))} и {list(filter(lambda x: result[x] > 1, result))} и {list(set(lst))}')
