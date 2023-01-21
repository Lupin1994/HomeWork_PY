# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
print('Enter coordinates of point A:')
x1 = int(input('Enter X1: '))
y1 = int(input('Enter Y1: '))
print(f'A({x1};{y1})')

print('Enter coordinates of point B:')
x2 = int(input('Enter X1: '))
y2 = int(input('Enter Y1: '))
print(f'B({x2};{y2})')

print(((x2-x1)**2 + (y2-y1)**2)**0.5)