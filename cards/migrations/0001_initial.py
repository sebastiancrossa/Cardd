# Generated by Django 2.0.7 on 2019-01-15 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=40)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('isPublic', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]