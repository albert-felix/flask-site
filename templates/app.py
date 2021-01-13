from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return('Homepage')

@app.route('/profile/<name>')
def profile(name):
    return(f"This is profile page of {name}")

@app.route('/admin')
def hello_admin():
    return("Hello Admin")

@app.route('/guest/<name>')
def hello_guest(name):
    return(f"Hello guest - {name}")

@app.route('/user/<user>')
def hello_user(user):
    if user == 'admin':
        return(redirect(url_for('hello_admin')))
    else:
        return(redirect(url_for('hello_guest', name=user)))


if __name__ == '__main__':
    app.run()