from flask import Flask, render_template, request, redirect
import mysql.connector
from config import db_config

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    address = request.form['address']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student (name, email, phone, course, address) VALUES (%s, %s, %s, %s, %s)",
                   (name, email, phone, course, address))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/students')

@app.route('/students')
def students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('students.html', students=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
