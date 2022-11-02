from datetime import datetime

class user:
    id = 0
    create_dt: datetime.now()
    tg_id = 0
    username = ""
    descrtext = ""
    first_token = ""
    token_requests_count = 0

    def createUserFromList(self, arr):
        self.id = arr.id
        self.create_dt = arr.create_dt
        self.tg_id = arr.tg_id
        self.username = arr.username
        self.descrtext = arr.descrtext
        self.first_token = arr.first_token
        self.token_requests_count = arr.token_requests_count

    def createUser(self, id, create_dt, tg_id, username, descrtext, first_token, token_requests_count):
        self.id = id
        self.create_dt = create_dt
        self.tg_id = tg_id
        self.username = username
        self.descrtext = descrtext
        self.first_token = first_token
        self.token_requests_count = token_requests_count

    



