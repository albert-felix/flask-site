from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def welcome(name):
    return(f"Welcome {name}")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return(redirect(url_for('welcome', name=username)))
    else:
        username = request.args.get('username')
        return(redirect(url_for('welcome', name=username)))



if __name__ == '__main__':
    app.run()