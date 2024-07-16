from flask import Flask, render_template
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password0'
)
print(mydb)
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register')
def Signin():
    return render_template('register.html')
if __name__ == "main":
    app.run(debug=True)