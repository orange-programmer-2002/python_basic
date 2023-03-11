from mysql.connector import MySQLConnection, Error

def connect():
    db_config = {
            'host': 'localhost',
            'database': 'pythonDb',
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
