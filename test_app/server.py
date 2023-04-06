from flask import Flask

app = Flask(__name__)

@app.route('/message')
def message():
    return 'Hello from Flask!'

if __name__ == '__main__':
    app.run()
