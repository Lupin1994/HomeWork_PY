# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#_________________________________________________________________________
# list = [2, 3, 5, 9, 3]
# Sum = 0
# for i in range (1,len(list),2):
#     Sum = Sum + list[i]
#     print(list[i],end=",")
# print()
# print(Sum)
#_________________________________________________________________________
from random import randint
list = [randint(0,100) for i in range(randint(5,10))]
print(list)
Sum = 0
for i in range (1,len(list),2):
    Sum += list[i]
    print(list[i],end=",")
print()
print(Sum)