from flask import Flask
from controllers.main_controller import index, insert, show_admin, submit, success, delete_user

app = Flask(__name__)

app.secret_key = 'Flask_Sectet_Key'

# define the routes and link them to the controller functions

app.add_url_rule('/', 'index', index)
app.add_url_rule('/insert', 'insert', insert)
app.add_url_rule('/show', 'show_admin', show_admin)
app.add_url_rule('/submit', 'submit', submit, methods=['POST'])
app.add_url_rule('/success', 'success', success)
app.add_url_rule('/delete/<int:delid>', 'delete_user', delete_user, methods=['POST', 'GET'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)