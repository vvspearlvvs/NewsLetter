## AWS 뉴스구독 서비스와 ELK 웹로그추척

<hr>

전체적인 진행과정은 블로그에서 확인할 수 있습니다: https://pearlluck.tistory.com/notice/479
추가) master브랜치 : Docker기반 ELK구축 

### 개요
구독이메일을 신청받는 Flask기반 웹서비스와 AWS의 새로운 소식을 매주 전달해주는 서비스 개발 및 AWS 운영


### 프로젝트 기간

2021.04.16 ~ 2021.05.14


### 사용기술

- Language : Python 3.6 <br>
- Web : Flask <br>
- OS : Ubuntu 20.4  <br>
- DB : Mysql 5.7 <br>
- Infra : AWS<br>
- API : AWS RSS feed

### 수행역할

- 구독 이메일을 신청 받을 수 있는 Flask 웹서비스 개발
- AWS What'new 소식을 크롤링하여 매주 이메일을 전달해주는 Python기반 서비스 개발
- AWS EC2, VPC, Route53, ELB 등 AWS환경구축 및 서비스 운영
- 서비스 기획부터 개발과 운영 그리고 유지보수까지 진행

### 아키텍쳐

1. 구독자가 http://www.what-news.shop 에 접속하여 이메일 구독 신청<br> (5월30일기준, 비용문제로 서비스중지)

2. 구독자 이메일  저장
3. 일정한 시간이 되면, AWS 신규소식을 RSS피드형식으로 크롤링
4. cron에 의해 스케쥴링 되어 이메일 전송

### ![newletter구조2](https://user-images.githubusercontent.com/78723318/118311484-edee3f80-b52a-11eb-848f-43b8bbaf6c9a.PNG)



### 프로젝트 결과

웹을 통해 구독을 신청한 이메일로 일정한 날짜와 시간이 되면, 자동으로 AWS 신규소식 메일을 전송한다.

![image-20210624161933371](https://user-images.githubusercontent.com/78723318/123601604-d812b080-d832-11eb-8036-5921f5a5ccb5.png)


### 추가진행예정 
- 단순한 HTML포맷 -> 카테고리별로 분류하는 등 가독성이 높은 메일포맷 변경 
- email전송 -> AWS SQS 서비스 기반 이메일 전송
- ELK스택을 사용한 웹로그 분석
