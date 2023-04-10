from flask import Flask, render_template, request
import json

app = Flask(__name__)

class User:
    def __init__(self, username, password, email) -> None:
        self.username = username
        self.password = password
        self.email = email

    def save_details(self):
        data = {
            "user" : self.username,
            "password": self.password,
            "email": self.email
        }
        with open("creds.json", "a") as f:
            # Write the JSON object to the file
            json.dump(data, f)
            # Add a newline character to separate the objects
            f.write('\n')
        
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
