from django.core.management.base import BaseCommand
from django.conf import settings

from telegramBot.models import AuthUser, Requests

import telebot

from datetime import datetime

from .Notifyer import Notifyer


def TryToFindUser(tg_id):
    users = AuthUser.objects.filter(tg_id=tg_id)[:1]
    if not users:
        return False
    return users[0]


def CheckToken(token):
    token = AuthUser.objects.filter(first_token=token)[:1]
    if not token:
        return False
    if token[0].tg_id != 0:
        token[0].token_requests_count += 1
        token[0].save()
        return False
    return token[0]


def AuthorizeUser(message, date):
    user = TryToFindUser(message.chat.id)
    if not user:
        print("not AuthorizeUser")
        freeToken = CheckToken(message.text)
        if not freeToken:
            print("not valid token")
            return False
        freeToken.date_joined = date
        freeToken.tg_id = message.chat.id
        freeToken.descrtext = ""
        freeToken.username = message.from_user.username
        freeToken.save()
        user = freeToken
    if user.token_requests_count >= settings.MAX_TOKEN_REQUEST:
        print("token_requests_count >= {}".format(settings.MAX_TOKEN_REQUEST))
        return False
    return user


def main():

    bot = telebot.TeleBot(settings.TOKEN)

    @bot.message_handler(content_types=['text'])
    def Request(message):
        formatted_date = datetime.utcfromtimestamp(int(message.date))\
            .strftime('%Y-%m-%d %H:%M:%S')
        print("Message Received: UserId: {}, Date: {}, MessageText: {}."
              .format(message.chat.id, formatted_date, message.text))

        user = AuthorizeUser(message, formatted_date)
        if not user:
            return

        print(user)

        Requests(tg_id=message.chat.id,
                 ts=formatted_date,
                 request_text=message.text).save()

        bot.send_message(message.chat.id, message.text)


    notifyer = Notifyer(settings.TIME_BETWEEN_NOTIFY, bot)
    notifyer.startNotifyLoop()

    print("TelegramBot started")

    bot.infinity_polling()
    notifyer.stopLoop()


class Command(BaseCommand):
    help = "Telegram bot start"

    def handle(self, *args, **options):
        main()
