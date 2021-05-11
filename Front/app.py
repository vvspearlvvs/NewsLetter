import Emailing
import Crawling
import Database
from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post',methods=['POST'])
def post():
    value=request.form['email']
    Database.insert_Email(value)
    print("이메일 저장 성공")

    #이메일저장하기

if __name__ == '__main__':
    app.run(host='0.0.0.0')
