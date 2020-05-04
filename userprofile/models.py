from django.db import models

# Create your models here.
from django.db.models.signals import post_save

from account.models import User


class FollowRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=11, verbose_name='电话号码')
    desc = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.FileField(upload_to='media/avatar/%Y/%m/%d/')
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


def user_did_save(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)


post_save.connect(user_did_save, sender=User)
