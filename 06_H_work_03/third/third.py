# 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
import random
a = [random.randint(1,10) for i in range(5)]
print(a)
res = [a[index]*a[-index-1]for index in range(len(a)//2+ len(a)%2)]
print(res)