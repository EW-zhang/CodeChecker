# Generated by Django 2.1 on 2019-04-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190409_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='username',
            field=models.CharField(max_length=150, verbose_name='用户名'),
        ),
    ]
