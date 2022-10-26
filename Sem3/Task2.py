# Напишите программу, которая определяет позицию второго вхождения
#  строки в списке, либо сообщит, что её нет.
test_list = ['123, 867, 987']
test_item = input("Введите исходную строку: ")
def check_list(test_list, test_item):
    count=0
    for i in range(len(test_list)):
        if test_list[i] == test_item:
            count += 1
            if count == 2:
                return i
    else:
        return -1
print(f'Ответ: {check_list(test_list, test_item)}')