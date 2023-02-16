# 45. Найти сумму чисел списка стоящих на нечетной позиции
import random
a = [random.randint(1,10) for i in range(6)]
print(a)
res = sum([value for indx,value in enumerate(a) if indx%2==1])
# res = list(map(lambda x: a[x] if (x)%2==1 else None,list(range(len(a)))))
# res = sum([i for i in res if i!=None])
print(res)