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
        insert_query = self.requests.insert().values(tg_id = tg_id, ts = ts, request_text = request_text)
        print("insertRequest SQL:")
        print(insert_query)
        self.myCon.execute(insert_query)

    def userInsert(self, user):
        insert_query = self.users.insert().values(create_dt = user.create_dt, tg_id = user.tg_id, username = user.username)
        print("userInsert SQL:")
        print(insert_query)
        self.myCon.execute(insert_query)

    def userAuthorization(self, id):
        query = db.select.where(self.users.columns.tg_id == id)
        ResultProxy = self.myCon.execute(query)
        ResultSet = ResultProxy.fetchall()
        print("userAuthorization SQL:")
        print(ResultSet)
        return ResultSet

    def createTableUsers(self):
        insert_query = "CREATE TABLE `users` (id int AUTO_INCREMENT NOT NULL,"\
        "create_dt TIMESTAMP NOT NULL DEFAULT NOW(),"\
        "tg_id INT NOT NULL DEFAULT 0,"\
        "username TEXT,"\
        "descrtext TEXT,"\
        "first_token TEXT,"\
        "PRIMARY KEY(id))"
        self.myCon.execute(insert_query)
    def createTableRequests(self):
        insert_query = "CREATE TABLE `requests` (id int AUTO_INCREMENT NOT NULL,"\
        "tg_id INT NOT NULL DEFAULT 0,"\
        "ts TIMESTAMP NOT NULL DEFAULT NOW(),"\
        "request_text TEXT,"\
        "PRIMARY KEY(id))"
        self.myCon.execute(insert_query)