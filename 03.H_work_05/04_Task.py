# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]
# def pos_fib(num):
#     pos_list = [1,1]
#     for i in range(num-2):
#         pos_list.append(pos_list[-2]+pos_list[-1])
#     return pos_list
# def neg_fib(num):
#     neg_list = [0,1]
#     for i in range(num-1):
#         neg_list.append(neg_list[-2]-neg_list[-1])
#     return neg_list[::-1] # переворот чисел с конца
# print(neg_fib(8)+pos_fib(8))
#_______________________________________________________
def pos_fib(num):
    pos_list = [1,1]
    for i in range(num-2):
        pos_list.append(pos_list[-2]+pos_list[-1])
    return pos_list
#[-1,1,0]=> [2,-1,1,0]=> [-3,2,-1,1,0]
def neg_fib(num):
    neg_list = [1,0]
    for i in range(num-1):
        neg_list.insert(0,neg_list[1]-neg_list[0])
    return neg_list # переворот чисел с конца
print(neg_fib(8)+pos_fib(8))