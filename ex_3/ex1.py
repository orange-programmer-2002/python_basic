import pandas as pd
from mysql.connector import MySQLConnection, Error

insertSql = "insert into students(id, code, first_name, last_name, birthOfDate, math, physics, chemistry) values (%s,%s,%s,%s,%s,%s,%s,%s)"
readSql = "select * from students"
deleteSql = "delete from students where name = %s"
updateSql = "update students set first_name = %s, last_name = %s where id = %s"

data = []

def connect():
    db_config = {
        'host': 'localhost',
        'database': 'ex3',
        'user': 'root',
        'password': '260349'
    }
    conn = None
    try:
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            return conn
    except Error as error:
        print(error)
    return conn

def loadData():
    try:
        conn = connect()
        cursor = conn.cursor()
        df = pd.read_excel('D:\input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)
        for row in df.iterrows():
            row_data = []
            for value in row[1]:
                row_data.append(value)
            val = (row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5],row_data[6],row_data[7])
            cursor.execute(insertSql, val)
            conn.commit()
            data.append(row_data)
    except:
        conn.rollback()
        conn.close()

def insertData(val):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(insertSql, val)
        conn.commit()
    except:
        conn.rollback()
        conn.close()

def readData():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(readSql)
        
        rs = cursor.fetchall()
        
        for x in rs:
            print(x)
    except:
        conn.rollback()
        conn.close()

def updateData(val):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(updateSql, val)
        conn.commit()
    except:
        conn.rollback()
        conn.close()

def deleteData(val):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(deleteSql, val)
        conn.commit()    
    except:
        conn.rollback()
        conn.close()