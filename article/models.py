from django.conf import settings
from django.db import models

# Create your models here.
from account.models import UserProfile


class ArticleLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users')
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name='articles')
    timestamp = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=140, verbose_name='博客内容')
    likes = models.ManyToManyField(UserProfile, related_name='user_like', blank=True, through=ArticleLike)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='articles')
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    @property
    def is_retweet(self):
        return self.parent is not None

    def __str__(self):
        return self.content
