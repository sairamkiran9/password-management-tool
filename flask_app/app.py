from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

class User:
    def __init__(self, username, password, email) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.create_creds()

    def create_creds(self):
        if not os.path.exists("creds.csv"):
            with open("creds.csv", "w+") as f:
                f.write("username,password,email\n")

    def save_details(self):
        data = self.username + "," + self.password + "," + self.email + "\n"
        with open("creds.csv", "a") as f:
            f.write(data)
        
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = User(username, password, email)
        user.save_details()
        return render_template('home.html', name=username)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return render_template('register.html', msg=msg)
    return render_template('register.html', msg=msg)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/", methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]
    return render_template("home.html", name=username)


if __name__ == "__main__":
    app.run(debug=True)
