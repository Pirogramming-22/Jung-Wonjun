from django.db import models

# Create your models here.
class Board(models.Model):
    GENRE_CHOICES = [
        ('Action', '액션'),
        ('Comedy', '코미디'),
        ('Drama', '드라마'),
        ('Fantasy', '판타지'),
        ('Horror', '호러'),
        ('SF', 'SF'),
    ]

    title = models.TextField()      # 제목
    year = models.IntegerField()    # 개봉년도

    genre = models.CharField(       # 장르
        max_length=10,
        choices=GENRE_CHOICES,
        blank=True
    )

    score = models.FloatField()     # 별점
    director = models.TextField()   # 감독
    actor = models.TextField()      # 배우
    runtime = models.IntegerField() # 러닝타임
    review = models.TextField()     # 리뷰 내용(본문)