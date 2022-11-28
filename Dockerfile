FROM python:3.9-alpine
LABEL vesion="1.0"

#RUN mkdir /usr/src/tgBot/
#WORKDIR /usr/src/telegramBot/
#WORKDIR /app

#RUN pip install --upgrade pip && \
#    pip install pyTelegramBotAPI && \
#    pip install PyYAML && \
#    pip install PyMySQL && \
#    pip install SQLAlchemy && \
#    pip install cryptography
#COPY requirements.txt .
RUN python3 -m pip install --upgrade pip

COPY . .

RUN pip install -r ./requirements.txt

#COPY . . 
	# /telegramBot/Consts.uaml . && \
	#/telegramBot/Consts.yaml . && \
	#/telegramBot/Notifyer.py . && \
#	/telegramBot/TelegramBot.py . && \
 #       /telegramBot/domain.py . && \
  #      /telegramBot/mysqllib.py . 

CMD ["python", "./telegramBot/TelegramBot.py"]
