# 45. Найти сумму чисел списка стоящих на нечетной позиции
import random
a = [random.randint(1,10) for i in range(6)]
print(a)
res = sum([value for indx,value in enumerate(a) if indx%2==1])
print(res)