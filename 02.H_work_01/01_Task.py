# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
#__________________________Первое решение____________________________________________
# num = str(input('Write number: '))
# sum = 0
# for i in range(len(num)):
#     sum = sum + int(num[i])
# print(sum)
#__________________________Второе решение______________________________________________
# n = input()
# sum = 0
# for i in n:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)
#__________________________Третье решение_______________________________________________

n = float(input())
len_num = len(str(n))-1
sum = 0
while n!=int(n):
    n= round(n*10,len_num)
    print(n)
while n>0:
    sum+=n%10
    n = n//10
print(sum)