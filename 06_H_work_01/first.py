# **44. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

a = [int(input(f'Write {i} coordinates point a - ')) for i in "xy"]
b = [int(input(f'Write {i} coordinates point a - ')) for i in "xy"]
res = sum([(element[1] - element[0])**2 for element in zip(a,b)])**0.5
print(res)