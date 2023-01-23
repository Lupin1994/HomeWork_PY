# 1.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# import random
# n = int(input())
# list_num = [random.randint(-n,n) for i in range(n)]
# print(list_num)

# file = open("File.txt","r")
# multi = 1
# list_str = file.readlines()
# list_num = list(map(str.strip,list_str))
# print(list_num)
# list_num = list(map(int,list_num))
# print(list_num)
# # for i in file:
# #     multi *= list_num[int(i)]
# print(multi)

# 2.Реализуйте алгоритм перемешивания списка.
# import random as r
# a = [1,2,3,4,5,6]
# r.shuffle(a)
# print(a)
#_______________________________________________________
# a = [1,2,3,4,5,6] 
# b = a  # в b передается не сам обьект а ссылка на него
# # по этому когда стираем данные с (a), они не появляюся в (b)
# a.clear()
# print(b)

# a = [1,2,3,4,5,6] 
# b = a.copy()
# a.clear()
# print(b)
#__________________________________________________________
import datetime
import random as r

def random_int(num):
    rand = datetime.datetime.now().microsecond/10**6
    return int(num*rand)

a = [1,2,3,4,5,6] 
random_int(5)
for i in range(len(a)-1,-1,-1):
    j = random_int(i+1)
    a[i],a[j] = a[j],a[i]
print(a)