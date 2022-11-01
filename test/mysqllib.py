import myuser
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, TIMESTAMP, Text
from sqlalchemy import insert
from sqlalchemy import MetaData

#meta = MetaData()
#requests = Table(
#   'requests', meta, 
#   Column('id', Integer, primary_key = True), 
#   Column('tg_id', Integer),
#   Column('timestamp', TIMESTAMP), 
#   Column('text', Text), 
#)

class mysqllib:
    def __init__(self, host, port, user, password, database):
        engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(user, password, host, port,database))
        self.myCon = engine.connect()
        print("Connected")

    def connectionClose(self):
        self.myCon.close()

    def insertRequest(self, tg_id, timestamp, text):
        insert_query = "INSERT INTO requests ("\
        "tg_id,"\
        "ts,"\
        "request_text) "\
        "VALUES ('{}', '{}', '{}');".format(tg_id, timestamp, text)#.format(id, tg_id, timestamp, text)
        print(insert_query)
        self.myCon.execute(insert_query)


    def userInsert(self, user):
        with self.myCon.cursor() as cursor:
            insert_query = "INSERT INTO users ("\
            "create_dt,"\
            "tg_id,"\
            "username)"\
            "VALUES ('{}', '{}', '{}');".format(user.create_dt, user.tg_id, user.username)
            cursor.execute(insert_query)
            self.myCon.commit()

    def userAuthorization(self, id):
        authorize_query = "SELECT * "\
        "FROM users "\
        "WHERE tg_id = {} "\
        "LIMIT 1".format(id)
        print(authorize_query)
        user = self.myCon.execute(authorize_query).fetchone()
        print(user)
        return user

    def createTableUsers(self):
        with self.myCon.cursor() as cursor:
            insert_query = "CREATE TABLE `users` (id int AUTO_INCREMENT NOT NULL,"\
            "create_dt TIMESTAMP NOT NULL DEFAULT NOW(),"\
            "tg_id INT NOT NULL DEFAULT 0,"\
            "username TEXT,"\
            "descrtext TEXT,"\
            "first_token TEXT,"\
            "PRIMARY KEY(id))"
            cursor.execute(insert_query)
            self.myCon.commit()
    def createTableRequests(self):
        with self.myCon.cursor() as cursor:
            insert_query = "CREATE TABLE `requests` (id int AUTO_INCREMENT NOT NULL,"\
            "tg_id INT NOT NULL DEFAULT 0,"\
            "ts TIMESTAMP NOT NULL DEFAULT NOW(),"\
            "request_text TEXT,"\
            "PRIMARY KEY(id))"
            cursor.execute(insert_query)
            self.myCon.commit()