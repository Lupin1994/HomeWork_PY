# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# N = int(input("Write number: "))
# Res = 1
# for i in range(1,N+1):
#     Res = Res*i
#     print(N, Res)

n = int(input())
fact_list = []
factorial = 1
for i in range(1,n+1):
    factorial*=i
    fact_list.append(factorial)
print(fact_list)