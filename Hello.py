
# типы данных и переменная
# int, float, boolean, str, list, None
value = None
a = 123
b = 1.23
# print(type(a))
# print(type(b))
value = 12334
# print(type(value))
s = 'hello world'

# print(s) # вывод строки
# print(a,'-',b,'-',s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
#print(f)


# list = [1,2,3,4]
# list2 = ['1','2','3','4','hello']
# print(list, list2)


# Ввод и вывод данных
# print input

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, '+' ,b, '=' ,a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции
# +, -, *, /(деление float), %(остаток от деления), 
# //(результат целое число), **(возведение в степень)
# **, +, -, *, /, %, //, +, -

# a=1.3
# b=3
# c=a*b
# c = round(a * b,3) #round округляет, а цифра, после запятой,
# указывает, сколько знаков показывать
# print(c)

# (), Сокращённые операции
# a = 3
# a = a + 5
# a += 5
# print(a)

# Логические операции:
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# Управляющие конструкции
# if, if-else, elif(условие в условии)
# a = int(input('a='))
# b = int(input('b='))
# if a > b:
#     print(a)
# else:
#     print(b)

# Цикл While и For
# a = 23
# b = 0
# while a !=0:
#     b=b*10+(a%10)
#     a//=10
# else:
#     print('Пожалуй')
#     print('Хорош')
# print(b) # Программа перевёртывания числа

# For
#1 for i in 1,2,3:
#       print(i**2)

#2 list=[1,2,3]
#  for i in list:
#      print(i**2)

# r = range(6, 22, 2)

# for i in 's_t_a_r-t':
#     print(i)

# Строки:
text = 'cъешь ещё этих мягких французских булок'
# print(text[0])
# print(text[1])
# print(text[len(text)-5])
# print(text[len(text)-1])
# print(text[-5])
# print(text[:])
# print(text[:])
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::5])

# print(len(text))              # 39
# print('ещё' in text)          # True
# print(text.isdigit())         # False
# print(text.islower())         # True
# print(text.replace('ещё этих', 'ЕЩЁ ЭтИх'))

# Списки: введение
# list == list
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# run = range(1, 6)
# numbers = list(run)
# print(numbers)
# numbers[0] = 10
# print(numbers)
# for i in numbers:
#     i*=2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)     # red green blue
# for e in colors:
#     print(e*2)   # redred greengreen blueblue

# colors.append('gray') # команда добавления в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True

# colors.remove('red') # del colors[0] # удаляет элемент
# print(colors)

# ФУНКЦИИ:
# def function_name(x): #так начинается ф-ия

def f(x):
    if x==1:
        return 'Целое'
    elif x==2.3:
        return 23
    else:
        return 'Не целое'
arg=1
print(f(arg))
print(type(f(arg))) # Показывает какой тип данных

