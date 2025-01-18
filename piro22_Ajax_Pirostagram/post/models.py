from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('게시물 이름:', max_length=20)
    image = models.ImageField('Image:', upload_to='uploaded_images/%Y%m%d', blank=True)
    content = models.TextField('게시물 내용:')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일")
    like = models.IntegerField()

    def __str__(self):
        return self.title