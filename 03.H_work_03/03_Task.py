# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
def drob(num):
    return round(num%1,2)

a = [round(random.uniform(0,10),2) for i in range(random.randint(5,8))]
print(a)
list_drob = list(map(drob,a))
print(list_drob)
print(max(list_drob), min(list_drob))
print(max(list_drob) - min(list_drob))
