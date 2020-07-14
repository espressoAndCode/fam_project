import mysql.connector 
import os



def connect():

    # print(f"config.host: {config.host}")
    # connecting to the database 
    dataBase = mysql.connector.connect( 
                        host = os.getenv('FAM_HOST'), 
                        user = os.getenv('FAM_USER'), 
                        passwd = os.getenv('FAM_PASS'), 
                        database = os.getenv('FAM_DB') ) 


    cursorObject = dataBase.cursor() 

    query = "SELECT * FROM FILESTATE"

    cursorObject.execute(query)

    res = cursorObject.fetchall()

    for item in res:
        print(item)

    # disconnecting from server 
    dataBase.close() 
