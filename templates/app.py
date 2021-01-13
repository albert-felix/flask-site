from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return('Homepage')

@app.route('/profile/<name>')
def profile(name):
    return(f"This is profile page of {name}")

if __name__ == '__main__':
    app.run()