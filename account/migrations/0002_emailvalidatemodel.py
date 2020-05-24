# Generated by Django 3.0.5 on 2020-05-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailValidateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now=True, verbose_name='添加时间')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('validate_code', models.CharField(max_length=20, verbose_name='验证码')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forgetpwd', '忘记密码')], default='register',
                                               max_length=50, verbose_name='类型')),
            ],
            options={
                'verbose_name': '邮箱验证码信息',
                'verbose_name_plural': '邮箱验证码信息',
            },
        ),
    ]