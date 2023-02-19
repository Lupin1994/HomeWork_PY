import telebot
import random

bot = telebot.TeleBot("6007940034:AAGXjfMypy9NJ-wbq_WFkwNRDUiq2YFozz4")

flag = None
sweets = 60
max_sweet = 20

@bot.message_handler(commands= ["start"])
def start(message):
    global flag
    bot.send_message(message.chat.id, f"Приветствую Вас в игре! ")
    flag = random.choice(["user","bot"])
    bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")
    if flag == "user":
        bot.send_message(message.chat.id, f"Первым ходите вы! ")
    else:
        bot.send_message(message.chat.id, f"Первым ходит Бот! ")
    
    controller(message)

def controller(message):
    global flag
    if sweets > 0 :
        if flag == "user":
            bot.send_message(message.chat.id, f"Ваш ход введите кол-во конфет от 0 до {max_sweet} ")
            bot.register_next_step_handler(message,user_input())
        else:
            bot_input(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Победил {flag}")    
def bot_input(message):
    global sweets,flag
    if sweets<=max_sweet:
        bot_turn = sweets
    elif sweets%max_sweet==0:
        bot_turn = max_sweet-1
    else:
        bot_turn = sweets%max_sweet-1
    sweets-=bot_turn
    bot.send_message(message.chat.id, f"Бот взял {bot_turn} конфет")
    bot.send_message(message.chat.id, f"Осталось {sweets} конфет")
    flag = "user" if flag == "bot" else "bot"  
    controller(message)      
def user_input(message):
    global sweets,flag
    user_turn = int(message.text)
    sweets-= user_turn
    bot.send_message(message.chat.id, f"Осталось {sweets} конфет")
    flag = "user" if flag == "bot" else "bot"
    controller(message)
    
bot.infinity_polling()