# INF601 - Advanced Programming in Python
# Lindsey Jimenez
# Mini Project 3

from flask import Flask

app = Flask(__name__)


@app.route('/admin')
def admin():  # put application's code here
    return 'administration page'


@app.route('/login')
def login():  # put application's code here
    return 'login page'


@app.route('/register')
def register():  # put application's code here
    return 'new member page'


@app.route('/')
def index():  # put application's code here
    return 'home page'


@app.route('/user/<username>')
def profile(username):  # put application's code here
    return f'{username}\'s profile page'


@app.route('/search')
def search():  # put application's code here
    return 'search page!'


if __name__ == '__main__':
    app.run()
