# Generated by Django 3.0.5 on 2020-04-23 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='context',
            new_name='content',
        ),
    ]
