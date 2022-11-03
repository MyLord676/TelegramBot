#import threading

#class Notifyer(object):
#    loop = 300
#    def changeTime(self, time):
#        self.loop = time
     
#    def startNotifyLoop(self, myBase, bot):
#        threading.Timer(self.loop, self.startNotifyLoop).start()
#        notifications = myBase.notifyGetAll()
#        sended = []
#        for n in notifications:
#            try:
#                bot.send_message(n.tg_id, n.notify_text)
#                sended.append(n.id)
#            except:
#                print("not sent: {}".format(n.id))
#        print("Notifications sent")
#        myBase.notifySended(sended)





