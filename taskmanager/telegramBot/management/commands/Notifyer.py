import threading
from telegramBot.models import Notify


class Notifyer(object):
    stopLoop = True

    def __init__(self, timeBetweenNotify, bot):
        self._timeBetweenNotify = timeBetweenNotify
        self.bot = bot

    def changeTime(self, time):
        self._timeBetweenNotify = time

    def stopLoop(self):
        self.stopLoop = False

    def startNotifyLoop(self):
        if not self.stopLoop:
            print("Notify ends")
            return
        threading.Timer(self._timeBetweenNotify, self.startNotifyLoop).start()
        notifications = Notify.objects.filter(sended=0)
        if not notifications:
            print("no notifications")
            return

        for n in notifications:
            try:
                self.bot.send_message(n.tg_id, n.notify_text)
                n.sended = 1
                n.save()
                print("send: {}".format(n))
            except Exception as e:
                print("not sent: {}".format(n))
                print(e)
        print("Notifications sent")
