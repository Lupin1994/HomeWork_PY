# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

Number = int(input('Write the number of quarter: '))
if Number >4 or Number <1:
    print('Try again')
    

if Number == 1:
    print('X>0 and Y>0')
elif Number == 2:
    print('X<0 and Y>0')
elif Number == 3:
    print('X<0 and Y<0')
elif Number == 4:
    print('X>0 and Y<0')
