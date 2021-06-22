from flask import Flask,request,flash,render_template,session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


@app.route('/')
def signup():
    return render_template('sign-up.html')


@app.route('/log-in')
def login():
    return render_template("log-in.html")


if __name__ == '__main__':
    app.run()
