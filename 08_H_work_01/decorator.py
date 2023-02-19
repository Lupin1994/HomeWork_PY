# import telebot
# bot = telebot.TeleBot("6128698085:AAHJr5DDQmD6Xf-SxSpuqBQsLRQ1SJvo_sM")

# def decorator(func):
#     import time
#     def wrapper(*args,**kwarge):
#         print("Its our programm")
#         start = time.time()
#         response = func(*args,**kwarge)
#         end = time.time()
#         print(f"Our function work for {end-start} second")
#         return response
#     return wrapper

# @decorator
# def request_url(url):
#     import requests
#     response = requests.get(url)
#     return response
# print(request_url("https://dzen.ru/?yredirect=true"))

# @bot.message_handler(commands=['start'])
# def start(message):
#     pass