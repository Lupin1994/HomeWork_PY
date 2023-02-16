# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def rle_decode(data_output):
        decoding = ''     
        i = 0     
        while i < len(data_output):        
            count = 0         
            while count < int(data_output[i]):            
                count += 1           
                decoding += data_output[i+1]      
                i += 2    
                return decoding
            
def rle_decoder(string):
    ini_str = ''
    for i in range(0, len(string), 2):
        ini_str += string[i + 1] * int(string[i])
    return ini_str

def encode(text):
    result = "" 
    count = 0    
    prev_char = text[0]    
    for char in text:         
        if char != prev_char:             
            result+=f"{count}{prev_char}"             
            prev_char = char             
            count = 1        
        else:             
            count+=1     
    else:         
        result+= f"{count}{prev_char}"     
    return result  

def decode(text):     
    result = ""    
    digit = True    
    count = 0   
    for char in text:     
        if digit:          
            count = int(char)             
            digit = False  
        else:          
            result+=count*char             
            digit = True
    return result  
text = 'aaaabbbbbccce' 
print(f'Исходный текст: {text}') 
encode_text = encode(text) 
decode_text = decode(encode_text)
print(f'Результат сжатия данных: {encode_text}') 
print(f'Результат разжатия данных: {decode_text}')