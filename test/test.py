from binascii import Error
from cmath import e
from multiprocessing import connection
from sqlite3 import Timestamp
from warnings import catch_warnings
from datetime import datetime, date, time
#from telebot import types
import pymysql
import telebot

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Alex9429",
        database="telegrambot",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connected")
    #try:
    #    with connection.cursor() as cursor:
    #        insert_query = "CREATE TABLE `requests2` (id int AUTO_INCREMENT NOT NULL,"\
    #        "tg_id int NOT NULL,"\
    #        "timestamp DATETIME NOT NULL,"\
    #        "request_text TEXT NOT NULL,"\
    #        "PRIMARY KEY(id))"
    #        cursor.execute(insert_query)
    #        connection.commit()
    #except Error as e:
    #    print("e")
    bot = telebot.TeleBot("5763587128:AAGBn7fDoFz1KgnoLoQd6YDmWq0x2SsKr2g")
    @bot.message_handler(content_types=['text'])
    def Request(message):
        bot.send_message(message.chat.id, message.text) 
        print("UserId: {}, Date: {}, MessageText: {}.".format(message.chat.id, message.date, message.text))
        try:
            with connection.cursor() as cursor:
                formatted_date = datetime.utcfromtimestamp(int(message.date)).strftime('%Y-%m-%d %H:%M:%S')
                #print(message.date)
                #print(datetime.now())
                #print(formatted_date)
                insert_query = "INSERT INTO requests2 (tg_id, timestamp, request_text) VALUES ({}, '{}', '{}');".format(message.chat.id, formatted_date, message.text)
                cursor.execute(insert_query)
                connection.commit()
        except Error as e:
            print(e)


    bot.polling(none_stop=True, timeout=123)
finally:
    connection.close()

