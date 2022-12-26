FROM python:3.9-alpine
LABEL vesion="1.0"

RUN mkdir /usr/src/tgBot/
WORKDIR /usr/src/tgBot/

RUN pip install --upgrade pip


#COPY ./Configs/* ./Configs/ 
COPY ./requirements.txt ./requirements.txt 
#COPY ./telegramBot/* ./telegramBot/


RUN pip install -r ./requirements.txt

CMD ["python", "./telegramBot/TelegramBot.py"]
