## ⏳ 개발 기간
**2022.09.08 ~ 2022.09.15**

</br>
  
## 🖥️ 프로젝트

#### 프로젝트 설명

- **요구사항**
- 제품 쇼핑몰 관리 페이지의 backend를 작성 합니다.
- 관리 페이지에는 다음의 기능이 제공 됩니다.
- 제품 주문 내역 열람
- 주문 내역 검색
- 주문 상태, 시작일자, 종료일자에 따른 필터
- 주문자명으로 검색
- 주문건에 대하여 발송 처리
- 쿠폰 관리
- 새로운 쿠폰 타입 신설
- 쿠폰은 다음의 방식이 있음
- 배송비 할인
- % 할인
- 정액 할인
- 특정 신규 쿠폰 코드 발급
- 발급된 쿠폰의 사용 내역 열람
- 쿠폰 타입 별 사용 횟수, 총 할인액
- 제품 배송 상태 업데이트
- 제품의 배송 상태를 배송 중, 배송 완료 등으로 수정 가능
- 간단히 구매 내역을 추가 할 수 있도록 구매하기 테스트 코드
- 쿠폰 사용에 따른 사용 할인 적용
- 구매 국가, 구매 갯수에 따른 배송비 적용
- 달러단위 배송비인 경우 일괄 1200원 = 1달러 로 적용하여 배송비를 추가 합니다.
- 일괄 적용이 아닌 현재 원-달러 환율을 가져와서 배송비를 적용 하는 경우 가산점을 부여 합니
다.
- 제공되는 데이터베이스는 쿠폰 시스템이 없는 데이터입니다.
- 쿠폰 시스템에 맞게 데이터베이스를 업데이트 하십시오.

<br/>

## 🧹 사용된 기술
- **Back-End** : Python, Django, Django REST framework
- **ETC** : Git, Github

</br>
## 🛠 Unit test



</br>

## ✍🏻 프로젝트 구현사항

- **주문내역 생성**
    -  로그인한 사용자만 주문 가능
    -  제품 수량, 도시, 나라, 우편번호, 쿠폰코드(없어도 가능)을 입력하여 주문 생성
    -  한국 외의 나라는 달러단위로 표시

- **주문내역 수정**
    -  결재상태 수정
    -  배송상태 수정

- **주문내역 겸색**
    -	 시작, 종료날짜, 결재상태, 주문자이름으로 검색
    -  
    