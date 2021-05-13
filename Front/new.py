import MongoDB
import sqlite3
import MysqlDB
import Emailing
import Crawling

def main():
    document_list = Crawling.get_crawling_aws() #aws데이터수집
    #MongoDB.insert_data(document_list) #디비저장

    html = Emailing.create_html(document_list) #메일보낼준비-메일내용생성

    #email_list = MongoDB.find_email('email') #메일보낼준비-수신자확인
    email_list = MysqlDB.find_email()
    for email in email_list:
        #email=email['email']
        Emailing.send_email(html,email) #메일전송-

if __name__ == '__main__':
    main()
