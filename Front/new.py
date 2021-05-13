#import Database
import sqlite3
import Emailing
import Crawling

def Database():
    email_list=[]
    conn = sqlite3.connect("emaildb.db", check_same_thread = False, isolation_level=None) #DB생성
    c=conn.cursor()

    c.execute("Select * FROM emails")
    receivers = c.fetchall() #list
    for receiver in receivers:
        email_list.append(receiver[0])
    return email_list

def main():
    #document_list = Crawling.get_crawling_aws() #aws데이터수집
    #Database.insert_data(document_list) #디비저장

    #html = Emailing.create_html(document_list) #메일보낼준비-메일내용생성

    '''
    email_list = Database.find_email('email') #메일보낼준비-수신자확인
    for receiver in email_list:
        email=receiver['email']
        Emailing.send_email(html,email) #메일전송-
     '''
    email_list = Database()
    for email in email_list:
        print("구독한 이메일들")
        print(email)
        #Emailing.send_email(html,email) #메일전송-

if __name__ == '__main__':
    main()
