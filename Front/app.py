import Database
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post',methods=['POST'])
def post():
    value=request.form['email']
    Database.insert_email(value)
    return render_template("index.html")

#추가로, 올바른 이메일인지 확인하는 검증하는 시스템까지 넣기

#특정시간이 되면 new.py 수행

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='80')
