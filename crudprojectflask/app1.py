# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, World!"

# if __name__=='__main__':
#     app.run(debug=True)

from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_connection():
    """ Create a database connection to the MySQL database """
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='onlinebooksreading'
        )
        if connection.is_connected():
            print("Connection successful")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

@app.route('/')
def index():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM admin")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', data=results)

if __name__ == '__main__':
    app.run(debug=True)