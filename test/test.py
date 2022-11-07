import telebot
import yaml
import threading

from datetime import datetime

import mysqllib
import domain


try:
    with open("Consts.yaml", "r") as yam:
        consts = yaml.safe_load(yam)
except Exception as e:
    print("Config 'Consts.yaml' do no read", e)

myBase = mysqllib.mysqllib(consts['host'], consts['port'],
                           consts['user'], consts['password'],
                           consts['database'])

bot = telebot.TeleBot(consts['token'])


@bot.message_handler(content_types=['text'])
def Request(message):
    formatted_date = datetime.utcfromtimestamp(int(message.date))\
        .strftime('%Y-%m-%d %H:%M:%S')
    print("Message Received: UserId: {}, Date: {}, MessageText: {}."
          .format(message.chat.id, formatted_date, message.text))

    authorizedUser = myBase.userAuthorization(message.chat.id)
    if not authorizedUser:
        newUser = myBase.tokenCheck(domain.User(
            create_dt=formatted_date,
            tg_id=message.chat.id,
            username=message.from_user.username,
            descrtext="",
            first_token=message.text,))
        if not newUser:
            return
        authorizedUser = newUser
    elif authorizedUser.token_requests_count >= consts['max_token_request']:
        return

    myBase.insertRequest(domain.Request(tg_id=message.chat.id,
                                        ts=formatted_date,
                                        request_text=message.text))

    bot.send_message(message.chat.id, message.text)


class Notifyer(object):
    _timeBetweenNotify = consts['timeBetweenNotify']

    def changeTime(self, time):
        self._timeBetweenNotify = time

    def startNotifyLoop(self):
        threading.Timer(self._timeBetweenNotify, self.startNotifyLoop).start()
        notifications = myBase.notifyGetAll()
        if not notifications:
            return

        sended = []
        for n in notifications:
            try:
                bot.send_message(n.tg_id, n.notify_text)
                sended.append(n.id)
            except Exception as e:
                print("not sent: {}".format(n.id))
                print(e)
        print("Notifications sent")
        myBase.notifySended(sended)


notifyer = Notifyer()
notifyer.startNotifyLoop()

while True:
    try:
        bot.polling(none_stop=True, timeout=10)
    except Exception as e:
        print(e)
