from flask import Flask, render_template
#import mysql.connector
#mydb = mysql.connector.connect(
#    host='localhost',
#    user='root',
#    passwd='password0'
#)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register')
def Signin():
    return render_template('register.html')
@app.route('/base')
def base():
    return render_template('base.html')
@app.route('/base/about')
def about():
    return render_template('about.html')
@app.route('/base/profile')
def profile():
    return render_template('profile.html')


if __name__ == "main":
    app.run(debug=True)