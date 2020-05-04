from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


# class UserFollow(models.Model):
#     idol = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='idols')
#     fan = models.ForeignKey('User', on_delete=models.CASCADE, related_name='fans')
#     timestamp = models.DateTimeField(auto_now_add=True)
