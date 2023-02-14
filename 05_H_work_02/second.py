# 39(1). Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, 
# вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой.
# В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 

# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, 
# позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить,
# соответственно внедрить этот алгоритм боту )
import random
def pvp():
    name1 = input("Введите имя первого игрока - ")
    name2 = input("Введите имя второго игрока - ")
    sweets = int(input("Введите желаемое количество конфет - "))
    max_sweets = int(input("Введите максимальное количество конфет за ход - "))
    
    first_turn = random.choice([name1,name2])
    
    flag = name1 if first_turn == name1 else name2
    
    while sweets>0:
        print(f'Ваш ход {flag}')
        turn = int(input("Введите количество конфет для взятия - "))
        while not 0< turn< max_sweets:
            print(f"Введите конфеты в диапазоне от 0 до {max_sweets}")
            turn = int(input("Введите количество конфет для взятия - "))
        sweets-=turn
        if sweets>0:
            print(f'конфет осталось - {sweets}')
        else:
            print(f'конфет осталось - 0')
            
        flag = name2 if flag == name1 else name1
    winner = name2 if flag == name1 else name1
            
    print(f'Поздравляем победил {winner}')
#pvp()

def pve_st():
    name1 = input("Введите имя первого игрока - ")
    name2 = "Bot"
    sweets = int(input("Введите желаемое количество конфет - "))
    max_sweets = int(input("Введите максимальное количество конфет за ход - "))
    
    
    first_turn = random.choice([name1,name2])
    
    flag = name1 if first_turn == name1 else name2
    
    while sweets>0:
        print(f'Ваш ход {flag}')
        if flag == name1:
            turn = int(input("Введите количество конфет для взятия - "))
            while not 0< turn< max_sweets:
                print(f"Введите конфеты в диапазоне от 0 до {max_sweets}")
                turn = int(input("Введите количество конфет для взятия - "))
            sweets-=turn
            if sweets>0:
                print(f'конфет осталось - {sweets}')
            else:
                print(f'конфет осталось - 0')
                
            flag = name2 if flag == name1 else name1
        else:
            turn = random.randint(1,max_sweets)
            print(f'Бот взял {turn} конфет')
            sweets-=turn
            if sweets>0:
                print(f'конфет осталось - {sweets}')
            else:
                print(f'конфет осталось - 0')
            flag = name2 if flag == name1 else name1
    winner = name2 if flag == name1 else name1
            
    print(f'Поздравляем победил {winner}')
# pve_st()
    
def pve_smart():
    name1 = input("Введите имя первого игрока - ")
    name2 = "Bot"
    sweets = int(input("Введите желаемое количество конфет - "))
    max_sweets = int(input("Введите максимальное количество конфет за ход - "))
    
    
    first_turn = random.choice([name1,name2])
    
    flag = name1 if first_turn == name1 else name2
    
    while sweets>0:
        print(f'Ваш ход {flag}')
        if flag == name1:
            turn = int(input("Введите количество конфет для взятия - "))
            while not 0< turn< max_sweets:
                print(f"Введите конфеты в диапазоне от 0 до {max_sweets}")
                turn = int(input("Введите количество конфет для взятия - "))
            sweets-=turn
            if sweets>0:
                print(f'конфет осталось - {sweets}')
            else:
                print(f'конфет осталось - 0')
                
            flag = name2 if flag == name1 else name1
        else:
            if sweets == max_sweets:
                turn = max_sweets
            elif sweets%max_sweets == 0:
                turn = max_sweets-1
            else:
                turn = sweets%max_sweets-1
                
            print(f'Бот взял {turn} конфет')
            sweets-=turn
            if sweets>0:
                print(f'конфет осталось - {sweets}')
            else:
                print(f'конфет осталось - 0')
            flag = name2 if flag == name1 else name1
    winner = name2 if flag == name1 else name1
            
    print(f'Поздравляем победил {winner}')    
pve_smart()