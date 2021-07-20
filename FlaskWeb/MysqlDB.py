import pymysql
mysql_host = 'localhost'
mysql_user = 'root'
mysql_pwd = 'qwer1234'
mysql_db = 'newdb'


#input email data
def insert_email(value1,value2):
    mysql_client = pymysql.connect(user=mysql_user,passwd=mysql_pwd,host=mysql_host,db=mysql_db,autocommit=True)
    cursor = mysql_client.cursor(pymysql.cursors.Cursor)
    input_sql="INSERT INTO emails values(%s,%s);"
    val = (value1,value2)
    cursor.execute(input_sql,val)

def find_email():
    email_list = []
    mysql_client = pymysql.connect(user=mysql_user,passwd=mysql_pwd,host=mysql_host,db=mysql_db,autocommit=True)
    cursor = mysql_client.cursor(pymysql.cursors.Cursor)
    cursor.execute("Select email FROM emails")
    receivers = cursor.fetchall()
    for receiver in receivers:
        email_list.append(receiver[0])
    return email_list
