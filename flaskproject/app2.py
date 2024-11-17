from flask import Flask, render_template, request, redirect, url_for
from db import create_connection

app = Flask(__name__)

app.secret_key = 'Flask_Sectet_Key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/show')
def show_admin():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    num_rows = len(results)
    return render_template('show.html', data=results, num_rows=num_rows)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO user (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    connection.commit()  # Commit the transaction
    cursor.close()
    connection.close()
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/delete/<int:delid>', methods=['POST','GET'])
def delete_user(delid):
    connection = create_connection()
    cursor = connection.cursor()
    # cursor.execute("DELETE FROM user WHERE id = %s', (delid,)")
    sql_query = "DELETE FROM user WHERE id = %s"
    cursor.execute(sql_query, (delid,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('show_admin'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)