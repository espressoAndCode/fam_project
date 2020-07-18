import mysql.connector 
import os
import datetime


def create_data(record):
    print(f"DB: {record}")
    # return


    # connecting to the database 
    cnx = mysql.connector.connect( 
                        host = os.getenv('FAM_HOST'), 
                        user = os.getenv('FAM_USER'), 
                        passwd = os.getenv('FAM_PASS'), 
                        database = os.getenv('FAM_DB') ) 


    cursor = cnx.cursor() 


# need to figure out datetime format
    # insert_stmt = ("INSERT INTO EVENTLOG VALUES ("datetime(record[0]), record[1], record[2], record[3], record[4], record[5]")")

    insert_stmt =  "INSERT INTO EVENTLOG (Timecode, Filepath, Syscall, Success, Exe, Auid) VALUES (%s, %s, %s, %s, %s, %s)"
    data_stmt = (record[0], record[1], record[2], record[3], record[4], record[5])

    # query = "SELECT * FROM FILESTATE"

    cursor.execute(insert_stmt, data_stmt)

    # res = cursorObject.fetchall()

    # for item in res:
    #     print(item)

    # disconnecting from server 


    cnx.commit()
    cursor.close()
    cnx.close() 

    # (
    #     Timecode        DATETIME            NOT NULL,
    #     Filepath        VARCHAR(255)        NOT NULL,
    #     Syscall         VARCHAR(64)         NOT NULL,
    #     Success         INT                 NOT NULL,
    #     Exe             VARCHAR(255)        NOT NULL,
    #     Auid            VARCHAR(64)         NOT NULL          
    # );









def read_data():

    # connecting to the database 
    cnx = mysql.connector.connect( 
                        host = os.getenv('FAM_HOST'), 
                        user = os.getenv('FAM_USER'), 
                        passwd = os.getenv('FAM_PASS'), 
                        database = os.getenv('FAM_DB') ) 


    cursor = cnx.cursor() 

    query = "SELECT * FROM FILESTATE"

    cursor.execute(query)

    res = cursor.fetchall()

    for item in res:
        print(item)

    # disconnecting from server 
    cnx.close() 
