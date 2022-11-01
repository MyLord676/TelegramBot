from cmath import e
from datetime import datetime
import mysqllib
import telebot
import yaml
import myuser
import mysqlalchemy

#t = mysqlalchemy.conn.execute("SELECT * "\
#    "FROM users").fetchall()
#print(t)

with open("Consts.yaml", "r") as yam:
    consts = yaml.safe_load(yam)
try:
    myBase = mysqllib.mysqllib(consts['host'], consts['port'], consts['user'], consts['password'], consts['database'])
    bot = telebot.TeleBot(consts['token'])

    

    @bot.message_handler(content_types=['text'])
    def Request(message):
        formatted_date = datetime.utcfromtimestamp(int(message.date)).strftime('%Y-%m-%d %H:%M:%S')
        print("UserId: {}, Date: {}, MessageText: {}.".format(message.chat.id, formatted_date, message.text))

        #if myBase.userAuthorization() != myuser.user:
        #    return
        #t = myBase.userAuthorization(message.chat.id)
        #myBase.TokenCheck(message.text)

        #u = myuser.user(0, formatted_date, message.chat.id, message.from_user.username, "", "")
        #myBase.userInsert(u)

        try:
            myBase.insertRequest(message.chat.id, formatted_date, message.text)
        except Error(e):
            print(e)
        bot.send_message(message.chat.id, message.text) 

    bot.polling(none_stop=True, timeout=123)
finally:
    myBase.connectionClose()


