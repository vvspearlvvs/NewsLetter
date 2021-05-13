import datetime
import sqlite3
from flask import Flask,render_template,request
app = Flask(__name__)

now=datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

def database(value1,value2):
    email_list=[]
    conn = sqlite3.connect("emaildb.db", isolation_level=None) #DB생성
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS emails(email varchar(256) PRIMARY KEY, sub_date datetime)")
    input_sql="INSERT INTO emails values(?,?);"
    c.execute(input_sql,(value1,value2))

    c.execute("Select email FROM emails")
    receivers = c.fetchall()
    for receiver in receivers:
        email_list.append(receiver[0])
    print(email_list)
    conn.close
    #print(c.fetchall())

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post',methods=['POST'])
def post():
    value=request.form['email']
    database(value,nowDatetime)
    #Database.insert_email(value)
    return render_template("index.html")

#추가로, 올바른 이메일인지 확인하는 검증하는 시스템까지 넣기

#특정시간이 되면 new.py 수행

if __name__ == '__main__':
    app.run(host='0.0.0.0')
