# Generated by Django 3.0.7 on 2020-07-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200711_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='mobile',
            field=models.IntegerField(blank=True, default=12345, max_length=15),
            preserve_default=False,
        ),
    ]
