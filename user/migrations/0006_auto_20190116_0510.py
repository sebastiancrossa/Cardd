# Generated by Django 2.0.7 on 2019-01-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190115_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to='media/profile_pics'),
        ),
    ]
