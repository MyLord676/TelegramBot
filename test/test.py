from datetime import datetime
import mysqllib
import telebot
import yaml
import myuser
import secrets

#print(secrets.token_hex(50)) #tokengenerator

try:
    with open("Consts.yaml", "r") as yam:
        consts = yaml.safe_load(yam)
except Error (e):
    print("Can't read config")
    print(e)

try:
    myBase = mysqllib.mysqllib(consts['host'], consts['port'], consts['user'], consts['password'], consts['database'])
except Error (e):
    print("Base crashed")
    print(e)

bot = telebot.TeleBot(consts['token'])

#myBase.createTableUsers()
#myBase.createTableRequests()

@bot.message_handler(content_types=['text'])
def Request(message):
    formatted_date = datetime.utcfromtimestamp(int(message.date)).strftime('%Y-%m-%d %H:%M:%S')
    print("Message Received: UserId: {}, Date: {}, MessageText: {}.".format(message.chat.id, formatted_date, message.text))

    try:    
        authorizedUser = myBase.userAuthorization(message.chat.id)
        if authorizedUser == False:
            newUser = myuser.user()
            newUser.createUser(0, formatted_date, message.chat.id, message.from_user.username, " ", message.text, 0)
            newUser = myBase.tokenCheck(newUser)
            if newUser == False:
                return
            myBase.userAdd(newUser)
            authorizedUser = newUser
        elif authorizedUser.token_requests_count >= consts['max_token_request']:
            return
    except Error(e):
        print("Authorization authentication error")
        print(e)

    myBase.insertRequest(message.chat.id, formatted_date, message.text)

    bot.send_message(message.chat.id, message.text) 


bot.polling(none_stop=True, timeout=123)
myBase.connectionClose()


