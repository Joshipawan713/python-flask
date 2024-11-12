from flask import Blueprint, render_template, request, redirect, url_for
from .models import UserModel

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/insert')
def insert():
    return render_template('insert.html')

@main.route('/show')
def show_admin():
    results = UserModel.get_all_users()
    num_rows = len(results)
    return render_template('show.html', data=results, num_rows=num_rows)

@main.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if not name or not email or not password:
        # flash("All fields are required.")
        return redirect(url_for('main.insert'))
    UserModel.insert_user(name, email, password)
    return redirect(url_for('main.success'))

@main.route('/success')
def success():
    return render_template('success.html')

@main.route('/delete/<int:delid>', methods=['POST'])
def delete_user(delid):
    UserModel.delete_user(delid)
    return redirect(url_for('main.show_admin'))