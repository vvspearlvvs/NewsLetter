# AWS 뉴스구독 서비스 
매주 AWS의 신규소식을 이메일로 전해주는 뉴스구독 서비스.
여기에서 >> http://www.what-news.shop << 구독할 이메일을 입력해주세요! 

### 전체적인 구조 
![newletter구조2](https://user-images.githubusercontent.com/78723318/118311484-edee3f80-b52a-11eb-848f-43b8bbaf6c9a.PNG)

### 사용한 기술 
Language : python 3.6 <br>
Web Framework : Flask <br>
OS : Ubuntu 20.4 (EC2)  <br>
DB : Mysql 5.7 <br>
AWS Service : VPC,IGW,ALB,EC2,ROUTE53 <br>

## 기타1 : Python 패키지
pip3 install flask <br>
pip3 install pytz <br>
pip3 install datetime <br>
pip3 install feedparser <br>
pip3 install googletrans==4.0.0-rc1 <br>
pip3 install smtplib 
pip3 install pymysql

### 기타2 : Mysql SQL문
mysql -u root -p <br>
create database mydb <br>
use mydb <br>
create table emails <br>
(emails varchar(256) primary key,sub_date datetime)

### 기타3 : crontab (UTC기준)
00 13 * * 2 ubuntu python3 /home/ubuntu/Newsletter/Front/new.app
