from flask import Flask, render_templatei, request, redirect,url_for
import mysql.connector

app=Flask(__name__)

db = mysql.connector.connect(
    host='localhost'
    user='root'
    password=''
    database='ders'
)

@app.route('/')
def index():
    return render_templatei('index.html')

@app.route('/signup')
def signup():
    return render_templatei('signup..html')

@app.route('/kayıtol')
def kayıtol():
    if request.method='POST':
        name=request.form['name']
        email=request.fom['email']
        password=request.form['password']


        cursoe=db.cursor()
        cursor.execute('INSERT INTO kullanıcı_bilgisi(name,email,password) VALUES(%s,%s,%s)',(name,email,password))
        db.commit()
        db.close()
        return redirect(url_for('index.html'))