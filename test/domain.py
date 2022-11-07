from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, SmallInteger, TIMESTAMP
from sqlalchemy.sql import func

Base = declarative_base()


class Notify(Base):
    __tablename__ = 'notify'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tg_id = Column(Integer, nullable=False, default=0)
    notify_text = Column(Text)
    sended = Column(SmallInteger, nullable=False, default=0)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    create_dt = Column(TIMESTAMP, nullable=False, default=func.now())
    tg_id = Column(Integer, nullable=False, default=0)
    username = Column(Text)
    descrtext = Column(Text)
    first_token = Column(Text)
    token_requests_count = Column(Integer, nullable=False, default=0)

    def exchangeFields(self, user):
        self.create_dt = user.create_dt
        self.tg_id = user.tg_id
        self.username = user.username
        self.descrtext = user.descrtext
        self.first_token = user.first_token
        self.token_requests_count = user.token_requests_count


class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tg_id = Column(Integer, nullable=False, default=0)
    ts = Column(TIMESTAMP, nullable=False, default=func.now())
    request_text = Column(Text)
