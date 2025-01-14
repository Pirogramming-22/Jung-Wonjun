from django.db import models
from apps.tool.models import Tool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('아이디어명:', max_length=20)
    image = models.ImageField('Image:', upload_to='uploaded_images/%Y%m%d', blank=True)
    content = models.TextField('아이디어 설명:')
    interest = models.IntegerField('아이디어 관심도:', max_length=20)
    devtool = models.ForeignKey(Tool, verbose_name='예상 개발툴:', on_delete=models.CASCADE)