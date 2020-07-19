import mysql.connector 
import os
import datetime


### data getters

def get_watches():
    watches = []
    cnx = mysql.connector.connect( 
                        host = os.getenv('FAM_HOST'), 
                        user = os.getenv('FAM_USER'), 
                        passwd = os.getenv('FAM_PASS'), 
                        database = os.getenv('FAM_DB') ) 
    cursor = cnx.cursor() 
    query = "SELECT * FROM WATCHES"
    cursor.execute(query)
    res = cursor.fetchall()

    for item in res:
        watches.append(item)

    cnx.close() 

    return watches


def read_data():
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

    cnx.close() 



### data setters

def create_watch(name, path):
    cnx = mysql.connector.connect( 
                        host = os.getenv('FAM_HOST'), 
                        user = os.getenv('FAM_USER'), 
                        passwd = os.getenv('FAM_PASS'), 
                        database = os.getenv('FAM_DB') ) 
    cursor = cnx.cursor() 
    insert_stmt =  "INSERT INTO WATCHES (Watchname, Filepath) VALUES (%s, %s)"
    data_stmt = (name, path)
    cursor.execute(insert_stmt, data_stmt)

    cnx.commit()
    cursor.close()
    cnx.close() 


def create_users (user_data):
    cnx = mysql.connector.connect( 
                        host = os.getenv('FAM_HOST'), 
                        user = os.getenv('FAM_USER'), 
                        passwd = os.getenv('FAM_PASS'), 
                        database = os.getenv('FAM_DB') ) 
    cursor = cnx.cursor() 
    insert_stmt =  "INSERT INTO AUTHORIZED (Watchname, Userid) VALUES (%s, %s)"
    cursor.executemany(insert_stmt, user_data)

    cnx.commit()
    cursor.close()
    cnx.close() 


def create_data(record):
    cnx = mysql.connector.connect( 
                        host = os.getenv('FAM_HOST'), 
                        user = os.getenv('FAM_USER'), 
                        passwd = os.getenv('FAM_PASS'), 
                        database = os.getenv('FAM_DB') ) 
    cursor = cnx.cursor() 
    insert_stmt =  "INSERT INTO EVENTLOG (Timecode, Filepath, Syscall, Success, Exe, Auid) VALUES (%s, %s, %s, %s, %s, %s)"
    data_stmt = (record[0], record[1], record[2], record[3], record[4], record[5])
    cursor.execute(insert_stmt, data_stmt)

    cnx.commit()
    cursor.close()
    cnx.close() 


def create_filestate(records):
    cnx = mysql.connector.connect( 
                        host = os.getenv('FAM_HOST'), 
                        user = os.getenv('FAM_USER'), 
                        passwd = os.getenv('FAM_PASS'), 
                        database = os.getenv('FAM_DB') ) 
    cursor = cnx.cursor() 
    insert_stmt =  "INSERT INTO FILESTATE (Filepath, Hashval, Timecode) VALUES (%s, %s, %s)"
    cursor.executemany(insert_stmt, records)

    cnx.commit()
    cursor.close()
    cnx.close() 

