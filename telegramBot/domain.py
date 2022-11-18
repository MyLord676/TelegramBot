from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, SmallInteger, TIMESTAMP, NVARCHAR, DateTime, null
from sqlalchemy.sql import func

Base = declarative_base()


class Notify(Base):
    __tablename__ = 'notify'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tg_id = Column(Integer, nullable=False, default=0)
    notify_text = Column(Text)
    sended = Column(SmallInteger, nullable=False, default=0)

    def __str__(self):
        return "id: {}||tg_id: {}|| notify_text: {}|| sended: {}"\
            .format(self.id, self.tg_id, self.notify_text, self.sended)


class auth_user(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tg_id = Column(Integer, nullable=False, default=0)
    username = Column(Text)
    descrtext = Column(Text)
    first_token = Column(Text)
    token_requests_count = Column(Integer, nullable=False, default=0)
    password = Column(NVARCHAR, nullable=False)
    last_login = Column(DateTime, nullable=null)
    is_superuser = Column(Integer, nullable=False)
    first_name = Column(NVARCHAR, nullable=False)
    last_name = Column(NVARCHAR, nullable=False)
    email = Column(NVARCHAR, nullable=False)
    is_staff = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)
    date_joined = Column(DateTime, nullable=False)

    def __str__(self):
        return "id: {}||tg_id: {}|| username: {}|| descrtext: {}||"\
            "first_token: {}|| token_requests_count: {}|| date_joined: {}"\
            .format(self.id, self.tg_id, self.username, self.descrtext,
                    self.first_token, self.token_requests_count, self.date_joined)

    def exchangeFields(self, user):
        self.date_joined = user.date_joined
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

    def __str__(self):
        return "id: {}||tg_id: {}|| request_text: {}|| ts: {}"\
            .format(self.id, self.tg_id, self.request_text, self.ts)
