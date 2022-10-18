# Напишите программу, которая на вход принимает 5
# чисел и находит максимальное из них
# print('Enter number a:')

# МОЙ ВАРИК
a = int(input('Enter number a:'))
b = int(input('Enter number b:'))
c = int(input('Enter number c:'))
d = int(input('Enter number d:'))
e = int(input('Enter number e:'))
numbs = [a, b, c, d, e]
print(numbs)
print(f'максимальное из {numbs} равно : {max(numbs)}')

# ВАРИК СТУДЕНТОВ
nums = input('Enter 5 nombers throught space:').split(' ')
max_num = int(nums[0])
for i in nums:
    if int(i) > max_num:
        max_num = int(i)
print(nums)
print(max_num)