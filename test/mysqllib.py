import sqlalchemy as db
from secrets import token_hex
from sqlalchemy.orm import Session

import domain


class mysqllib:
    def __init__(self, host, port, user, password, database):
        self.engine = db.create_engine("mysql+pymysql://{}:{}@{}:{}/{}"
                                       .format(user, password,
                                               host, port, database))
        self.meta = db.MetaData()
        print("Connected to mysql")

    """Insert request to database"""
    def insertRequest(self, request: domain.Request):
        session = Session(self.engine)
        try:
            session.add(request)
            session.commit()
            return request
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    """Generate new token in database"""
    def addToken(self):
        token = token_hex(50)
        session = Session(self.engine)
        try:
            session.add(domain.User(first_token=token))
            session.commit()
            return token
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    """Check if id of user telegram exists in database"""
    def userAuthorization(self, tg_id):
        session = Session(self.engine)
        try:
            user = session.query(domain.User)\
                .filter(domain.User.tg_id == tg_id).first()
            if not user:
                return False
            return user
        except Exception as e:
            print(e)
        finally:
            session.close()

    """Try to find token in database and create a new user if successes"""
    def tokenCheck(self, user: domain.User):
        session = Session(self.engine)
        try:
            tokenFromDb: domain.User = session.query(domain.User)\
                .filter(domain.User.first_token == user.first_token).first()

            if not tokenFromDb:
                return False
            if tokenFromDb.tg_id != 0:
                tokenFromDb.token_requests_count += 1
                session.commit()
                return False
            tokenFromDb.create_dt = user.create_dt
            tokenFromDb.tg_id = user.tg_id
            tokenFromDb.username = user.username
            tokenFromDb.descrtext = user.descrtext
            tokenFromDb.token_requests_count = tokenFromDb.token_requests_count

            session.commit()

            user.id = tokenFromDb.id
            user.token_requests_count = tokenFromDb.token_requests_count
            return user
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    """Add notify to database"""
    def notifyAdd(self, notify: domain.Notify):
        session = Session(self.engine)
        try:
            session.add(notify)
            session.commit()
            return notify
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    def notifyGetAll(self):
        session = Session(self.engine)
        try:
            notifications = session.query(domain.Notify)\
                .filter(domain.Notify.sended == 0).all()
            return notifications
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    """Change notify status to sent"""
    def notifySended(self, arr):
        session = Session(self.engine)
        try:
            for n in arr:
                notifications = session.query(domain.Notify).get(n)
                notifications.sended = 1
                session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

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

    def createTableNotify(self):
        query = "CREATE TABLE `notify` (id int AUTO_INCREMENT NOT NULL,"\
                "tg_id INT NOT NULL DEFAULT 0,"\
                "notify_text TEXT,"\
                "sended SMALLINT NOT NULL DEFAULT 0,"\
                "PRIMARY KEY(id))"
        self.myCon.execute(query)
