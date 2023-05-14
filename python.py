from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    if user:
        # User is authenticated, redirect to homepage
        return redirect('/')
    else:
        # Authentication failed, show error message
        return render_template('login.html', error='Invalid username or password')

if __name__ == '__main__':
    app.run(debug=True)
