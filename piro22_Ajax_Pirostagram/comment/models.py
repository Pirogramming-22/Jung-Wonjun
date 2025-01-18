from django.db import models
from post.models import Post

# Create your models here.
class Comment(models.Model):
    content = models.TextField('댓글 내용:')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')