# PiroStagram

## 실행 방법1
```Bash
1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver
```

## 실행 방법2
```Bash
1. pip install django
2. pip install Pillow
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver
```

## 구현한 기능
- 좋아요
- 댓글 작성
- 댓글 삭제

## 챌린지
- 실제 인스타 ui에 맞춰서 구현하기

## 기능 설명
### 메인 페이지
- 게시한 게시물의 수만큼 메인 페이지 상단 게시물 수 실시간 변경
- 게시물 작성 버튼 클릭시 게시물 작성 페이지로 이동
- 게시물 사진 클릭시 게시물 상세 페이지로 이동

### 게시물 작성 페이지
- form을 통해서 게시물 작성 가능

### 게시물 상세 페이지
- 하트 모양 클릭 시 좋아요 수 증가
- 댓글 모양 클릭 시 댓글창 페이지로 이동
- 상단바의 프로필 클릭시 메인 페이지로 돌아감

### 댓글창 페이지
- 페이지 하단의 form을 이용하여 댓글을 달 수 있음
- 작성한 댓글은 상단에 바로 추가되어 보여짐
- 쓰레기통 모양 클릭시 댓글별 삭제 가능
- 스크롤로 댓글 전부 확인 가능
- 상단의 '댓글' 글씨 부분 클릭시 다시 게시물 상세 페이지로 돌아감