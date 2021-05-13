import pymysql

#mongodb
mysql_host = 'localhost'
mysql_user = 'root'
mysql_pwd = ''
mysql_db = 'mydb'

mysql_client = pymysql.connect(user=mysql_user,passwd=mysql_pwd,host=mysql_host,db=mysql_db)

#input email data
def insert_email(value1,value2):
    cursor = mysql_client.cursor(pymysql.cursors.Cursor)
    input_sql="INSERT INTO emails values(?,?);"
    cursor.execute(input_sql,(value1,value2))

def find_email():
    email_list = []
    cursor = mysql_client.cursor(pymysql.cursors.Cursor)
    cursor.execute("Select email FROM emails")
    receivers = cursor.fetchall()
    for receiver in receivers:
        email_list.append(receiver[0])
    return email_list
