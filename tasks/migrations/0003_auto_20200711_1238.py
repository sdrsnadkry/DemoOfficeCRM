# Generated by Django 3.0.7 on 2020-07-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_userdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='code',
            field=models.IntegerField(blank=True),
        ),
    ]
