import datetime
import sqlite3
import MysqlDB
from flask import Flask,render_template,request
app = Flask(__name__)

now=datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post',methods=['POST'])
def post():
    value=request.form['email']
    #MongoDB.insert_email(value)
    MysqlDB.insert_email(value,nowDatetime)
    return render_template("index.html")

#추가로, 올바른 이메일인지 확인하는 검증하는 시스템까지 넣기
#특정시간이 되면 new.py 수행

if __name__ == '__main__':
    app.run(host='0.0.0.0')
