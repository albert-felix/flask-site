from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return(render_template('home.html'))

@app.route('/welcome/<username>')
def welcome(username):
    return(render_template('welcome.html', name = username))


if __name__ == '__main__':
    app.run()