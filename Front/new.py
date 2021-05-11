import Database
import Emailing
import Crawling

def main():
    document_list = Crawling.get_crawling_aws() #aws데이터수집
    Database.insert_data(document_list) #디비저장

    html = Emailing.create_html(document_list) #메일보낼준비-메일내용생성

    email_list = Database.find_email('email') #메일보낼준비-수신자확인
    for receiver in email_list:
        receiver=receiver['email']
        Emailing.send_email(html,receiver) #메일전송

if __name__ == '__main__':
    main()
