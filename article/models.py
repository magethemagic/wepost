from django.conf import settings
from django.db import models

# Create your models here.
from account.models import User


class ArticleLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name='articles_like')
    timestamp = models.DateTimeField(auto_now_add=True)


class ArticleTags(models.Model):
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, related_name='tags')
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name='articles_tag')


class Tag(models.Model):
    name = models.CharField(max_length=100)
    article = models.ManyToManyField("Article", related_name='articles_of_a_tag', blank=True, through=ArticleTags)

    def __str__(self):
        return self.name


class Article(models.Model):
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    content = models.CharField(max_length=140, verbose_name='博客内容')
    likes = models.ManyToManyField(User, related_name='user_like', blank=True, through=ArticleLike)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    tags = models.ManyToManyField(Tag, related_name='article_tags', blank=True, through=ArticleTags)

    class Meta:
        ordering = ['-id']

    @property
    def is_retweet(self):
        return self.parent is not None

    def __str__(self):
        return self.content


class Comment(models.Model):
    content = models.CharField(max_length=140, verbose_name='评论内容')
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercomments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content
