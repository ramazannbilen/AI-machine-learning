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

#update code
cursor = mydb.cursor()
username = "ali"
email = "veli@gmail.com"
password = '123asd'
userid = 4

cursor.execute("UPDATE users SET username = %s, email = %s, password = %s WHERE userid = %s",(username, email, password,userid))
mydb.commit()


#delete code
cursor2 = mydb.cursor()
userid = 2

cursor2.execute('DELETE FROM users WHERE userid = %s ', (userid,))
mydb.commit()

mydb.close()

if __name__=='__main__':
    app.run(debug=True)   
     
