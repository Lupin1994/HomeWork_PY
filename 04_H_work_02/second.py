# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input())
res_list =[]
cur_num = 2
while n!=1:
    if n%cur_num ==0:
        res_list.append(cur_num)
        n = n//cur_num
        cur_num = 2
    else:
        cur_num+=1
print(res_list)