from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class EmailValidateModel(models.Model):
    timestamp = models.DateField(verbose_name=u'添加时间', auto_now=True)
    email = models.EmailField(verbose_name=u'邮箱')
    validate_code = models.CharField(max_length=20, verbose_name=u'验证码')

    # 新加send_type类型
    send_type = models.CharField(max_length=50, verbose_name=u'类型',
                                 choices=(('register', u'注册'), ('forgetpwd', u'忘记密码')), default='register')

    class Meta:
        verbose_name = u'邮箱验证码信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.email
