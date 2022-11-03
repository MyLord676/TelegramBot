from datetime import datetime
import mysqllib
import telebot
import yaml
import domain

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

#############################################################
#myBase.addToken()
#myBase.createTableUsers()
#myBase.createTableRequests()
#myBase.createTableNotify()
#myBase.notifyAdd(domain.Notify(notify_text = "test2"))
#print (myBase.addToken())
#myBase.userAddTokenRequest(domain.User(id = 2, create_dt = '2022-11-02 12:33:00', tg_id = 1855954960, username = 'AlexEltc', descrtext = "test", token_requests_count = 0))
#print(myBase.userAuthorization(1855954960).id)
#############################################################

@bot.message_handler(content_types=['text'])
def Request(message):
    formatted_date = datetime.utcfromtimestamp(int(message.date)).strftime('%Y-%m-%d %H:%M:%S')
    print("Message Received: UserId: {}, Date: {}, MessageText: {}.".format(message.chat.id, formatted_date, message.text))

    try:    
        authorizedUser = myBase.userAuthorization(message.chat.id)
        if authorizedUser == False:
            newUser = myBase.tokenCheck(
                domain.User(create_dt = formatted_date, 
                            tg_id = message.chat.id, 
                            username = message.from_user.username, 
                            descrtext = "", first_token = message.text,)
                )
            if newUser == False:
                return
        elif authorizedUser.token_requests_count >= consts['max_token_request']:
            return
    except Error(e):
        print("Authorization authentication error")
        print(e)

    myBase.insertRequest(domain.Request(tg_id = message.chat.id,ts = formatted_date, request_text = message.text))

    bot.send_message(message.chat.id, message.text) 


bot.polling(none_stop=True, timeout=123)


