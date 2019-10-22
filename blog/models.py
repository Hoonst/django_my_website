from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    #글 제목
    title = models.CharField(max_length =30)
    #글 내용
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)


    #날짜
    created = models.DateTimeField()
    #작성자
    author = models.ForeignKey(User, on_delete=True)

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)