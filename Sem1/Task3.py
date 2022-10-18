# Напишите программу, которая принимает число N
#  и выводит числа от -N до N
N = int(input('Enter number N:'))
#ВАРИАНТ 1:
for i in range(-N, N + 1):
    print(i, end=', ')
# ВАРИАНТ 2:
print(*range(-N, N + 1), sep=', ')
# ВАРИАНТ 3
print(*range(-(N:=int(input('Enter number N:'))), N + 1), sep=', ')