# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# list = [2, 3, 4, 5, 6]
# listNew = []
# product = 0
# I_max = len(list)-1
# for i in range(len(list)):
#     if i != I_max-i:
#         product = list[i]*list[I_max-i]  
#         print(product)
#____________________________________________________________________________
list = [2, 3, 5, 6]
listNew = []
middle = len(list)//2 + len(list)%2
for i in range(middle):
    listNew.append(list[i]*list[-i-1])
print(listNew)