import mysql.connector
from mysql.connector import Error

def create_connection():
    """ Create a database connection to the MySQL database """
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='book_ciil'
        )
        if connection.is_connected():
            print("Connection successful")
    except Error as e:
        print(f"Error: '{e}'")
    return connection