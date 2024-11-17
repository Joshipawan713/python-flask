from db import create_connection
import mysql.connector
from mysql.connector import Error


# def get_all_users():
#     connection = create_connection()
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM user")  # Change table and columns as per your schema
#     results = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return results

def get_all_users():
    connection = create_connection()
    if connection is None:
        print('Failed to connect to database')
        return []
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM user')
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        results = []
    finally:
        cursor.close()
        connection.close()
    return results
        

def insert_user(name,email,password):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO user(name,email,password) VALUES(%s, %s, %s)", (name,email,password))
    connection.commit()
    cursor.close()
    connection.close()
    
def delete_user_by_id(user_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM user WHERE id = %s", (user_id,))
    connection.commit()
    cursor.close()
    connection.close()