# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет
a = int(input("Write the number of day: "))
if a>7 or a<1:
    print("Try again.")
elif a == 6 or a ==7:
    print('Good news for every one!!! Today is a day off.')
else:
    print('Get to work, you lazy ass!')