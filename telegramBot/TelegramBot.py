import telebot
import yaml

from datetime import datetime

import mysqllib
import domain
import Notifyer


def main():
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
            newUser = myBase.tokenCheck(domain.auth_user(
                date_joined=formatted_date,
                tg_id=message.chat.id,
                username=message.from_user.username,
                descrtext="",
                first_token=message.text,))
            if not newUser:
                return
            authorizedUser = newUser

        if authorizedUser.token_requests_count >= consts['max_token_request']:
            return

        print(authorizedUser)

        myBase.insertRequest(domain.Request(tg_id=message.chat.id,
                                            ts=formatted_date,
                                            request_text=message.text))

        bot.send_message(message.chat.id, message.text)

    notifyer = Notifyer.Notifyer(consts['timeBetweenNotify'], bot, myBase)
    notifyer.startNotifyLoop()

    bot.infinity_polling()
    notifyer.stopLoop()


if __name__ == '__main__':
    main()
