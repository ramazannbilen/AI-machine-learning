from flask import Flask, render_template, request,redirect,url_for

import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="registration",
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cursor = mydb.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES(%s, %s, %s)',( username, email, password))
        mydb.commit()
        mydb.close()
        return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)   
     
