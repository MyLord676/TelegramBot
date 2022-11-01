import pymysql
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
    def insertRequest(self, id, date, text):
        with self.myCon.cursor() as cursor:
            insert_query = "INSERT INTO requests2 ("\
            "tg_id,"\
            "timestamp,"\
            "request_text)"\
            "VALUES ({}, '{}', '{}');".format(id, date, text)
            cursor.execute(insert_query)
            self.myCon.commit()
    
    #try:
    #    with connection.cursor() as cursor:
    #        insert_query = "CREATE TABLE `requests2` (id int AUTO_INCREMENT NOT NULL,"\
    #        "tg_id int NOT NULL,"\
    #        "timestamp DATETIME NOT NULL,"\
    #        "request_text TEXT NOT NULL,"\
    #        "PRIMARY KEY(id))"
    #        cursor.execute(insert_query)
    #        connection.commit()
    #except Error as e:
    #    print("e")