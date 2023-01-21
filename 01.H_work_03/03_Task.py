# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
print('I will show you where you are ')

X = int(input('Write your X: '))
Y = int(input('Write your Y: '))

if X>0 and Y>0:
    print('You are in the first quarter')
elif X<0 and Y>0:
    print('You are in the second quarter')
elif X<0 and Y<0:
    print('You are in the third quarter')
else:
    print('You are in the fourth quarter')