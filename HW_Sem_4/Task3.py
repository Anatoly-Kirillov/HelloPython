# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.
numbers_list = list(map(int, input('Введите последовательность чисел: ').split()))
unique_list = []
numbers_list.sort()
current = 0
while current < len(numbers_list):
    check = numbers_list.count(numbers_list[current])
    if check > 1:
        for i in range(check):
            numbers_list.remove(numbers_list[current])
    else:
        unique_list.append(numbers_list[current])
        numbers_list.remove(numbers_list[current])
print(unique_list)