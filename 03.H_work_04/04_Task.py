# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def dec_to_bin(num,result = ""):
    if num ==0:
        return result
    result = str(num%2)+result
    return dec_to_bin(num//2,result)
print(dec_to_bin(int(input())))