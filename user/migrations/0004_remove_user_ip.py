# Generated by Django 2.0.7 on 2019-01-15 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190115_0358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ip',
        ),
    ]