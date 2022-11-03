from email.policy import default
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer, Text, SmallInteger, TIMESTAMP
from sqlalchemy.sql import func

Base = declarative_base()

class Notify(Base):
    __tablename__ = 'notify'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tg_id = Column(Integer, nullable=False, default = 0)
    notify_text = Column(Text)
    sended = Column(SmallInteger, nullable=False, default = 0)

class User(Base):
   __tablename__ = "users"

   id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
   create_dt = Column(TIMESTAMP, nullable=False, default = func.now())
   tg_id = Column(Integer ,nullable=False, default = 0)
   username = Column(Text)
   descrtext = Column(Text)
   first_token = Column(Text)
   token_requests_count = Column(Integer, nullable=False, default = 0)

   def exchangeFields(self, user):
       self.create_dt = user.create_dt
       self.tg_id = user.tg_id
       self.username = user.username
       self.descrtext = user.descrtext
       self.first_token = user.first_token
       self.token_requests_count = user.token_requests_count

   #def createUserFromList(self, arr):
   #     self.id = arr.id
   #     self.create_dt = arr.create_dt
   #     self.tg_id = arr.tg_id
   #     self.username = arr.username
   #     self.descrtext = arr.descrtext
   #     self.first_token = arr.first_token
   #     self.token_requests_count = arr.token_requests_count

   # def createUser(self, id, create_dt, tg_id, username, descrtext, first_token, token_requests_count):
   #     self.id = id
   #     self.create_dt = create_dt
   #     self.tg_id = tg_id
   #     self.username = username
   #     self.descrtext = descrtext
   #     self.first_token = first_token
   #     self.token_requests_count = token_requests_count

class Request(Base):
   __tablename__ = 'requests'

   id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
   tg_id = Column(Integer ,nullable=False, default = 0)
   ts = Column(TIMESTAMP, nullable=False, default = func.now())
   request_text = Column(Text)
   

