from flask import render_template, request, redirect, url_for
from models.user_model import get_all_users, insert_user, delete_user_by_id

# Home page route
def index():
    return render_template('index.html')

# Insert page route
def insert():
    return render_template('insert.html')

# Show admin route
def show_admin():
    users = get_all_users() #get all users from the model
    num_rows = len(users)
    return render_template('show.html', data=users, num_rows=num_rows)

# Submit from route
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    insert_user(name,email,password)
    return redirect(url_for('success'))

# Success page route
def success():
    return render_template('success.html')

# delete user route
def delete_user(delid):
    delete_user_by_id(delid)
    return redirect(url_for('show_admin'))