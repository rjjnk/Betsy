import os
from flask import Flask, redirect, render_template, request, session, url_for, flash
from helpers import verify_password

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def frontpage():
    return render_template("home_page.html")

@app.route('/home/')
def home():
    return redirect(url_for("frontpage"))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        login_succesfull = verify_password(username, password)
        if login_succesfull:
            session["user"] = username
            return redirect(url_for("frontpage"))
        else:
            return redirect(url_for('login'))
    else:
        if "user" in session:
            return redirect(url_for("frontpage"))
        return render_template('log_in.html')

@app.route('/sign_up/', methods=['GET', 'POST'])
def sign_up():
#     if request.method == "POST":
    return render_template("sign_up.html")

if __name__ == "__main__":
    app.run(debug=True)