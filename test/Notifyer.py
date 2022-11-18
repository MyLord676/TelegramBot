import threading


class Notifyer(object):
    stopLoop = True

    def __init__(self, timeBetweenNotify, bot, base):
        self._timeBetweenNotify = timeBetweenNotify
        self.bot = bot
        self.myBase = base

    def changeTime(self, time):
        self._timeBetweenNotify = time
    
    def stopLoop(self):
        self.stopLoop = False

    def startNotifyLoop(self):
        if not self.stopLoop:
            print("Notify ends")
            return
        print("Notify start {}".format(self._timeBetweenNotify))
        threading.Timer(self._timeBetweenNotify, self.startNotifyLoop).start()
        notifications = self.myBase.notifyGetAll()
        if not notifications:
            print("not notifications")
            return

        sended = []
        for n in notifications:
            try:
                self.bot.send_message(n.tg_id, n.notify_text)
                sended.append(n.id)
            except Exception as e:
                print("not sent: {}".format(n.id))
                print(e)
        print("Notifications sent")
        self.myBase.notifySended(sended)
