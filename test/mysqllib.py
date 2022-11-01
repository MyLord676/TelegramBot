import pymysql
import myuser
class mysqllib:
    def __init__(self, host, port, user, password, database):
        self.myCon = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected")

    def connectionClose(self):
        self.myCon.close()

    def insertRequest(self, id, tg_id, timestamp, text):
        with self.myCon.cursor() as cursor:
            insert_query = "INSERT INTO requests ("\
            "tg_id,"\
            "ts,"\
            "request_text)"\
            "VALUES ('{}', '{}', '{}');".format(tg_id, timestamp, text)
            cursor.execute(insert_query)
            self.myCon.commit()

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
        with self.myCon.cursor() as cursor:
            authorize_query = "SELECT TOP(1)"\
            "FROM users"\
            "WHERE tg_id = id"
            cursor.execute(authorize_query)
            id, create_dt, tg_id, username, descrtext, first_token = cursor.fetchone()
            user = myuser.user(id, create_dt, tg_id, username, descrtext, first_token)
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