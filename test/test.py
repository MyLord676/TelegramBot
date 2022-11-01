from datetime import datetime
import mysqllib
import telebot
import yaml

with open("Consts.yaml", "r") as yam:
    consts = yaml.safe_load(yam)
try:
    myBase = mysqllib.mysqllib(consts['host'], consts['port'], consts['user'], consts['password'], consts['database'])
    bot = telebot.TeleBot(consts['token'])

    @bot.message_handler(content_types=['text'])
    def Request(message):
        formatted_date = datetime.utcfromtimestamp(int(message.date)).strftime('%Y-%m-%d %H:%M:%S')
        print("UserId: {}, Date: {}, MessageText: {}.".format(message.chat.id, formatted_date, message.text))



        try:
            myBase.insertRequest(message.chat.id, formatted_date, message.text)
        except Error as e:
            print(e)  
        bot.send_message(message.chat.id, message.text) 

    bot.polling(none_stop=True, timeout=123)
finally:
    myBase.connectionClose()


