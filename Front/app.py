import datetime
from pytz import timezone
import MysqlDB
from flask import Flask,render_template,request
app = Flask(__name__)

now=datetime.datetime.now(timezone('Asia/Seoul'))
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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
