from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    # extract user data from form
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    
    # validate user data
    # ...

    # save user data to database or data file
    # ...

    return 'Registration successful!'


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
