from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.TextField()      # 제목
    year = models.TextField()       # 개봉년도
    genre = models.TextField()      # 장르
    score = models.TextField()      # 별점
    director = models.TextField()   # 감독
    actor = models.TextField()      # 배우
    runtime = models.TextField()    # 러닝타임
    review = models.TextField()     # 리뷰 내용(본문)