# Generated by Django 3.0.5 on 2020-05-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('userprofile', '0003_auto_20200504_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Female'), ('F', 'Female')], default='Male', max_length=7),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(upload_to='../media/avatar/%Y/%m/%d/'),
        ),
    ]