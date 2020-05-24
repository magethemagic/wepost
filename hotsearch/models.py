from django.db import models


# Create your models here.
class SearchKey(models.Model):
    key_content = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
