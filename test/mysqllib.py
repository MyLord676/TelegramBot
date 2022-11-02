import myuser
import sqlalchemy as db

class mysqllib:
    def __init__(self, host, port, user, password, database):
        engine = db.create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(user, password, host, port,database))
        self.myCon = engine.connect()
        self.meta = db.MetaData()
        self.requests = db.Table('requests', self.meta, autoload=True, autoload_with=engine)
        self.users = db.Table('users', self.meta, autoload=True, autoload_with=engine)
        print("Connected to mysql")

    def connectionClose(self):
        self.myCon.close()

    def insertRequest(self, tg_id, ts, request_text):
        query = self.requests.insert().values(tg_id = tg_id, ts = ts, request_text = request_text)
        print("insertRequest SQL:")
        print(query)
        self.myCon.execute(query)

    def userAdd(self, user: myuser.user):
        query = self.users.update().\
        values(create_dt = user.create_dt,
               tg_id = user.tg_id,
               username = user.username,
               descrtext = user.descrtext).where(self.users.columns.id == user.id)
        print("userAdd SQL:")
        print(query)
        self.myCon.execute(query)

    def tokenInsert(self, first_token):
        query = self.users.insert().values(first_token = first_token)
        print("tokenInsert SQL:")
        print(query)
        self.myCon.execute(query)

    def userAuthorization(self, id):
        query = db.select([self.users]).where(self.users.columns.tg_id == id).limit(1)
        ResultProxy = self.myCon.execute(query)
        ResultSet = ResultProxy.fetchall()
        print("userAuthorization SQL:")
        print(ResultSet)
        if not ResultSet:
            return False
        user = myuser.user()
        user.createUserFromList(ResultSet[0])
        return user

    def tokenCheck(self, user: myuser.user):
        query = db.select([self.users]).where(self.users.columns.first_token == user.first_token).limit(1)
        ResultProxy = self.myCon.execute(query)
        ResultSet = ResultProxy.fetchall()
        print("tokenCheck SQL:")
        print(ResultSet)
        if not ResultSet:
            return False
        userWithToken = myuser.user()
        userWithToken.createUserFromList(ResultSet[0])
        if userWithToken.tg_id != 0:
            self.userAddTokenRequest(userWithToken)
            return False
        newUser = myuser.user()
        newUser.createUser(userWithToken.id, user.create_dt, user.tg_id, user.username, user.descrtext, userWithToken.first_token, userWithToken.token_requests_count)
        return newUser

    def userAddTokenRequest(self, user):
        query = self.users.update().\
        values(token_requests_count = user.token_requests_count + 1).where(self.users.columns.id == user.id)
        print("userAddTokenRequest SQL:")
        print(query)
        self.myCon.execute(query)
        
    def createTableUsers(self):
        query = "CREATE TABLE `users` (id int AUTO_INCREMENT NOT NULL,"\
        "create_dt TIMESTAMP NOT NULL DEFAULT NOW(),"\
        "tg_id INT NOT NULL DEFAULT 0,"\
        "username TEXT,"\
        "descrtext TEXT,"\
        "first_token TEXT,"\
        "token_requests_count INT NOT NULL DEFAULT 0,"\
        "PRIMARY KEY(id))"
        self.myCon.execute(query)

    def createTableRequests(self):
        query = "CREATE TABLE `requests` (id int AUTO_INCREMENT NOT NULL,"\
        "tg_id INT NOT NULL DEFAULT 0,"\
        "ts TIMESTAMP NOT NULL DEFAULT NOW(),"\
        "request_text TEXT,"\
        "PRIMARY KEY(id))"
        self.myCon.execute(query)